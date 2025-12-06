import streamlit as st
import pandas as pd
import altair as alt
import io

# -------------------------------------------------
# Page setup
# -------------------------------------------------
st.set_page_config(
    page_title="Civic Indicators – Reporting Tool",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Civic Indicators – Domain-based Reporting Tool")
st.markdown(
    """
    **Explore domain-based indicators over time.**
    
    Use the sidebar to filter data and customize the visualization.
    """
)

# -------------------------------------------------
# Load & reshape data
# -------------------------------------------------
@st.cache_data
def load_long_data(path: str = "Results.xlsx", sheet: str = "Sheet1") -> pd.DataFrame:
    try:
        raw = pd.read_excel(path, sheet_name=sheet)

        # Assume first two columns are Domain and Question
        col0, col1 = raw.columns[0], raw.columns[1]
        raw = raw.rename(columns={col0: "Domain", col1: "Question"})

        # First row holds year information for each country column
        year_row = raw.iloc[0]

        # Data rows start from row index 1
        data = raw.iloc[1:].reset_index(drop=True)

        # Columns containing numeric values (one per country–wave)
        value_cols = [c for c in data.columns if c not in ["Domain", "Question"]]

        # Clean labels
        data["Domain"] = data["Domain"].astype(str).str.strip()
        data["Question"] = data["Question"].astype(str).str.strip()

        # Long format
        long_df = data.melt(
            id_vars=["Domain", "Question"],
            value_vars=value_cols,
            var_name="col",
            value_name="value"
        )

        # Country from column name; Year from first row
        long_df["Country"] = long_df["col"].astype(str).str.split(".").str[0]
        long_df["Year"] = long_df["col"].apply(lambda c: int(year_row[c]))

        # Drop missing values
        long_df = long_df.dropna(subset=["value"])

        return long_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()


long_df = load_long_data()

if long_df.empty:
    st.stop()

# -------------------------------------------------
# Sidebar controls
# -------------------------------------------------
st.sidebar.header("⚙️ Configuration")

# --- Data Selection ---
with st.sidebar.expander("1. Data Selection", expanded=True):
    # Domain
    domains = sorted(long_df["Domain"].unique())
    selected_domain = st.selectbox("Domain", domains)
    
    dom_df = long_df[long_df["Domain"] == selected_domain]
    
    # Questions within domain
    questions = sorted(dom_df["Question"].unique())
    default_q = [questions[0]] if questions else []
    selected_questions = st.multiselect(
        "Indicators (questions)",
        questions,
        default=default_q
    )
    
    # Countries
    countries = sorted(dom_df["Country"].unique())
    selected_countries = st.multiselect(
        "Countries",
        countries,
        default=countries
    )
    
    # Year range
    years = sorted(dom_df["Year"].unique())
    if years:
        y_min, y_max = int(min(years)), int(max(years))
        selected_year_range = st.slider(
            "Year range",
            y_min, y_max,
            (y_min, y_max)
        )
    else:
        selected_year_range = (0, 0)

# --- Visual Settings ---
with st.sidebar.expander("2. Visual Settings", expanded=False):
    # Chart Type
    chart_type = st.selectbox(
        "Chart Type",
        ["Line Chart", "Bar Chart"],
        index=0
    )

    # Layout
    layout = st.radio(
        "Plot layout",
        ["Single figure (all countries)", "Country panels"],
        index=0
    )
    
    # Show column control if we are faceting (either by country or by indicator)
    show_grid_control = (layout == "Country panels") or (layout == "Single figure (all countries)" and len(selected_questions) > 1)
    
    grid_columns = 2
    if show_grid_control:
        grid_columns = st.slider("Grid columns (width)", 1, 6, 2)


    
    # Graph style
    graph_style = st.selectbox(
        "Graph style",
        [
            "Colorblind-safe (default)",
            "Monochrome (blue shades)",
            "Black & white (line styles)",
            "Highlight focal country"
        ],
        index=0
    )
    
    # Theme presets
    theme = st.selectbox(
        "Theme preset",
        [
            "Academic (light)",
            "OECD grey",
            "Dark dashboard",
            "Pastel report",
            "The Economist",
            "Financial Times"
        ],
        index=0
    )
    
    # Focal country
    focal_country = None
    if graph_style == "Highlight focal country":
        focal_country = st.selectbox(
            "Focal country",
            countries,
            index=0
        )

# -------------------------------------------------
# Filtered data for plotting
# -------------------------------------------------
if not selected_questions or not selected_countries:
    st.warning("Please select at least one indicator and one country.")
    st.stop()

plot_df = dom_df[
    (dom_df["Question"].isin(selected_questions)) &
    (dom_df["Country"].isin(selected_countries)) &
    (dom_df["Year"].between(selected_year_range[0], selected_year_range[1]))
]

if plot_df.empty:
    st.warning("No data for this combination. Try widening the year range or adding countries.")
    st.stop()

# Check for missing countries
present_countries = set(plot_df["Country"].unique())
missing_countries = set(selected_countries) - present_countries
if missing_countries:
    st.warning(f"⚠️ The following countries have no data for the selected period and are not shown: {', '.join(sorted(missing_countries))}")


# -------------------------------------------------
# Main Content: Dashboard Layout
# -------------------------------------------------

# --- 1. KPI Metrics ---
m1, m2, m3, m4 = st.columns(4)
m1.metric("Countries", len(selected_countries))
m2.metric("Indicators", len(selected_questions))
m3.metric("Years", f"{selected_year_range[0]} - {selected_year_range[1]}")
m4.metric("Data Points", len(plot_df))

st.divider()

# --- 2. Chart Section ---
st.subheader(f"📈 Analysis: {selected_domain}")

# --- Style helpers ---
def get_country_color_encoding():
    """Color mapping for countries, depending on graph style."""
    if graph_style == "Colorblind-safe (default)":
        palette = [
            "#1b9e77", "#d95f02", "#7570b3", "#e7298a",
            "#66a61e", "#e6ab02", "#a6761d", "#666666"
        ]
        return alt.Color(
            "Country:N",
            title="Country",
            scale=alt.Scale(range=palette)
        )

    if graph_style == "Monochrome (blue shades)":
        return alt.Color(
            "Country:N",
            title="Country",
            scale=alt.Scale(scheme="blues")
        )

    if graph_style == "Highlight focal country" and focal_country is not None:
        return alt.condition(
            alt.datum.Country == focal_country,
            alt.value("#1f77b4"),   # highlight
            alt.value("#CCCCCC")    # others
        )

    return alt.value("black")


def get_stroke_dash_encoding():
    """Line style mapping (used for black & white)."""
    if graph_style == "Black & white (line styles)":
        return alt.StrokeDash(
            "Country:N",
            title="Country",
            sort=selected_countries
        )
    return alt.value([1, 0])


def style_chart(chart: alt.Chart) -> alt.Chart:
    """Apply theme preset: fonts, fill, grid, legend, etc."""
    chart = chart.configure_axis(
        labelFontSize=13,
        titleFontSize=15
    ).configure_legend(
        titleFontSize=14,
        labelFontSize=12
    ).configure_title(
        fontSize=18,
        anchor="start"
    )

    if theme == "Academic (light)":
        chart = chart.configure_view(strokeWidth=0, fill="white").configure_axis(grid=True, gridColor="#DDDDDD")
    elif theme == "OECD grey":
        chart = chart.configure_view(stroke="#CCCCCC", strokeWidth=1, fill="white").configure_axis(grid=True, gridColor="#E0E0E0")
    elif theme == "Dark dashboard":
        chart = chart.configure_view(strokeWidth=0, fill="#111111").configure_axis(
            labelColor="white", titleColor="white", grid=True, gridColor="#333333"
        ).configure_legend(titleColor="white", labelColor="white").configure_title(color="white")
    elif theme == "Pastel report":
        chart = chart.configure_view(strokeWidth=0, fill="#FAFAFA").configure_axis(grid=True, gridColor="#F0F0F0")
    elif theme == "The Economist":
        # Economist style: Blue-gray background, horizontal grid only usually, but we keep grid simple
        chart = chart.configure_view(strokeWidth=0, fill="#d5e4eb").configure_axis(
            grid=True, gridColor="white", labelFont="Verdana", titleFont="Verdana"
        ).configure_title(font="Verdana", fontSize=20).configure_legend(labelFont="Verdana", titleFont="Verdana")
    elif theme == "Financial Times":
        # FT style: Salmon/Pinkish background
        chart = chart.configure_view(strokeWidth=0, fill="#fff1e0").configure_axis(
            grid=True, gridColor="#e3cbb0", labelFont="Georgia", titleFont="Georgia"
        ).configure_title(font="Georgia", fontSize=20).configure_legend(labelFont="Georgia", titleFont="Georgia")

    return chart

color_encoding = get_country_color_encoding()
stroke_dash_encoding = get_stroke_dash_encoding()

# --- Plotting Logic ---
# --- Plotting Logic ---

def create_single_chart(data, title_text, x_axis_title="Year", y_axis_title="Value", color_enc=None, dash_enc=None, x_off=None):
    base = alt.Chart(data)
    if chart_type == "Bar Chart":
        mark = base.mark_bar()
    else:
        mark = base.mark_line(point=True)
    
    chart = mark.encode(
        x=alt.X("Year:O", title=x_axis_title),
        y=alt.Y("value:Q", title=y_axis_title),
        color=color_enc,
        strokeDash=dash_enc,
        xOffset=x_off,
        tooltip=["Country", "Year", "Question", "value"]
    ).properties(
        title=title_text,
        height=450 # Fixed height, width will be responsive
    )
    return style_chart(chart)

if layout == "Single figure (all countries)":
    if len(selected_questions) > 1:
        # Multiple indicators -> Grid of charts, one per indicator
        cols = st.columns(grid_columns)
        for i, q in enumerate(selected_questions):
            # Filter data for this question
            q_data = plot_df[plot_df["Question"] == q]
            
            # Create chart
            chart = create_single_chart(
                q_data, 
                title_text=f"{q}",
                y_axis_title="Value",
                color_enc=color_encoding,
                dash_enc=stroke_dash_encoding if chart_type == "Line Chart" else alt.value([0,0]),
                x_off="Country:N" if chart_type == "Bar Chart" else alt.value(0)
            )
            
            # Place in column
            with cols[i % grid_columns]:
                st.altair_chart(chart, use_container_width=True)
                
    else:
        # One indicator -> Single chart
        chart = create_single_chart(
            plot_df,
            title_text=f"{selected_questions[0]} – {selected_domain}",
            y_axis_title=selected_questions[0],
            color_enc=color_encoding,
            dash_enc=stroke_dash_encoding if chart_type == "Line Chart" else alt.value([0,0]),
            x_off="Country:N" if chart_type == "Bar Chart" else alt.value(0)
        )
        st.altair_chart(chart, use_container_width=True)

else:
    # Country panels -> Grid of charts, one per country
    if graph_style == "Black & white (line styles)":
        panel_color = alt.value("black")
        panel_dash = alt.StrokeDash("Question:N", title="Indicator")
    else:
        panel_color = alt.Color("Question:N", title="Indicator")
        panel_dash = alt.value([1, 0])
        
    cols = st.columns(grid_columns)
    for i, country in enumerate(selected_countries):
        # Filter data for this country
        c_data = plot_df[plot_df["Country"] == country]
        
        if c_data.empty: continue

        # Create chart
        chart = create_single_chart(
            c_data,
            title_text=f"{country}",
            y_axis_title="Value",
            color_enc=panel_color,
            dash_enc=panel_dash if chart_type == "Line Chart" else alt.value([0,0]),
            x_off="Question:N" if chart_type == "Bar Chart" else alt.value(0)
        )
        
        # Place in column
        with cols[i % grid_columns]:
            st.altair_chart(chart, use_container_width=True)



# --- 3. Footer / Export ---
st.divider()
with st.expander("📥 Export & Data View", expanded=False):
    c1, c2 = st.columns([1, 3])
    with c1:
        st.markdown("### Download")
        csv = plot_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download CSV",
            csv,
            "filtered_data.csv",
            "text/csv",
            key='download-csv',
            use_container_width=True
        )
        
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            plot_df.to_excel(writer, sheet_name='Data', index=False)
        
        st.download_button(
            "Download Excel",
            buffer.getvalue(),
            "filtered_data.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key='download-excel',
            use_container_width=True
        )
    
    with c2:
        st.markdown("### Raw Data Preview")
        st.dataframe(plot_df, height=200, use_container_width=True)

