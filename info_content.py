variable_info_md = """
# Operationalisation Table

| Variable | Domain | Items Used | Method | Interpretation |
|---------|--------|------------|--------|----------------|
| D1_Justification | Citizenship | F115–F117 | Mean | Justification tendencies |
| D1_Participation | Citizenship | E025–E029 | Count "1" | Number of unconventional political acts |
| D1_02a Participation scaled | Citizenship | E025–E029 | D1_02 / 5 | Proportion of unconventional acts |
| D1_Political Interest | Citizenship | E023, E150 | Reverse + Mean | Higher = more political interest |
| D2_Membership | Citizenship | A065–A074 | Count | Civic engagement breadth |
| D2_Proud of Nationality | Citizens–State | G006 | Reverse (5 - G006) | Strength of national pride |
| D3_Confidence in Institutions | Citizens–State | E069_01–E069_17 | PCA (reversed) | Trust in institutions |
| D3_Confidence in the EU | Citizens–State | E069_18 | Reverse | Trust in supranational authority |
| D3_Support for Technocray&Authoritarianism | Citizens–State | E114–E116 | PCA | Support for non-democratic rule |
| D3_Support for Democracy | Citizens–State | E117 (+E114–E116 via PCA) | PCA | Democratic support |
| D5_Belief in Democracy | Legitimacy | E120–E123 | PCA | Perceived legitimacy of democracy |
| D6_Protestant Ethic | Legitimacy/Resilience | C036–C041 | PCA | Meritocratic, effort-based norms |
| Agency | Legitimacy/Resilience | A173 | Raw | Perceived freedom/control |
| D4_01 Concern for Everyone | Social Cohesion | E154–E158 | PCA (reversed) | Universal concern |
| D4_02 Concern for Vulnerable | Social Cohesion | E159–E162 | PCA (reversed) | Solidarity with disadvantaged |
| D4_Independence vs. Obedience | Social Cohesion | A029–A042 | (Autonomy – Conformity) | Value orientation |
| D04_Autonomy-oriented child qualities | Social Cohesion | A029, A030, A034, A039 | Additive | Emphasis on autonomy |
| D04_Conformity-oriented child qualities | Social Cohesion | A038, A040, A042 | Additive | Emphasis on obedience |
| D04_Prosocial/communal child qualities | Social Cohesion | A032, A035, A041 | Additive | Emphasis on relational values |
| D4_Gender Discrimination | Justice/Cohesion | D059–D060 | Formula | Gender equality views |
| D4_04A Gender Equality (factor) | Justice/Cohesion | D059–D060 | PCA | Coherent equality index |
| D4_AntiImmigrant | Justice/Cohesion | C002 | Recode -2..1 | Exclusion of immigrants |
| D4_Intolerance | Justice/Cohesion | A124_02,05,06,10 | Count | General intolerance |
| D4_Moral_Intolerance | Justice/Cohesion | A124_03,08,09 | Count | Moralised exclusion |
| D4_Generalized Trust | Cohesion/Resilience | A165 | Binary (1 only) | Trust in others |
| D5_ProMarket | Justice/Fairness | E035–E039 | PCA | Preference for markets vs redistribution |
| Satisfaction with Life | Resilience | A170 | Raw | Subjective well-being |


# Item-Level Descriptions

## National Identity & CSO Membership
- G006 — How proud of nationality  
- A065 — Member: Religious organisation  
- A066 — Member: Education, arts, music, culture  
- A067 — Member: Labour unions  
- A068 — Member: Political parties  
- A069 — Member: Local political actions  
- A070 — Member: Human rights organisation  
- A071 — Member: Conservation/environment/animal rights  
- A072 — Member: Professional associations  
- A073 — Member: Youth work  
- A074 — Member: Sports or recreation  

## Institutional Confidence (E069 Block)
- E069_01 — Confidence: Churches  
- E069_02 — Confidence: Armed Forces  
- E069_03 — Confidence: Education System  
- E069_04 — Confidence: Press  
- E069_05 — Confidence: Labour Unions  
- E069_06 — Confidence: Police  
- E069_07 — Confidence: Parliament  
- E069_08 — Confidence: Civil Services  
- E069_09 — Confidence: Social Security System  
- E069_11 — Confidence: Government  
- E069_12 — Confidence: Political Parties  
- E069_13 — Confidence: Major Companies  
- E069_14 — Confidence: Environmental Protection Movement  
- E069_16 — Confidence: Health Care System  
- E069_17 — Confidence: Justice System / Courts  
- E069_18A — Confidence: Regional organisation  
- E069_18 — Confidence: European Union  
- E069_19 — Confidence: NATO  
- E069_20 — Confidence: United Nations  

## Views on Governance
- E114 — Political system: Strong leader  
- E115 — Experts make decisions  
- E116 — Army rule  
- E117 — Democratic political system  

## Social Concern
- E154 — Concern: Neighbourhood  
- E155 — Concern: Region  
- E156 — Concern: Fellow countrymen  
- E157 — Concern: Europeans  
- E158 — Concern: Humankind  
- E159 — Concern: Elderly  
- E160 — Concern: Unemployed  
- E161 — Concern: Immigrants  
- E162 — Concern: Sick/disabled  

## Childrearing Values (A029–A042)
- A029 — Independence  
- A030 — Hard work  
- A032 — Responsibility  
- A034 — Imagination  
- A035 — Tolerance & respect  
- A038 — Thrift  
- A039 — Determination  
- A040 — Religious faith  
- A041 — Unselfishness  
- A042 — Obedience  

## Gender Attitudes (D059–D062)
- D059 — Men make better political leaders than women  
- D060 — University more important for boys  
- D061 — Pre-school child suffers if mother works  
- D062 — Women want home and children  

## Job Scarcity & Outgroups
- C001 — Jobs scarce: Men should have priority  
- C002 — Jobs scarce: Employers should favour nationals  

## Intolerance / Social Distance
- A124_02 — Neighbours: People of different race  
- A124_03 — Neighbours: Heavy drinkers  
- A124_05 — Neighbours: Muslims  
- A124_06 — Neighbours: Immigrants  
- A124_08 — Neighbours: Drug addicts  
- A124_09 — Neighbours: Homosexuals  
- A124_10 — Neighbours: Jews  

## Trust
- A165 — Most people can be trusted  

## Democratic Legitimacy (E120–E123)
- E120 — Democracy: Economic system runs badly  
- E121 — Democracy: Indecisive / too much squabbling  
- E122 — Democracy: Not good at maintaining order  
- E123 — Democracy better despite problems  

## Economic Preferences (E035–E039)
- E035 — Income equality  
- E036 — Private vs state ownership  
- E037 — Government responsibility  
- E038 — Job-taking of unemployed  
- E039 — Competition good/harmful  

## Work Ethic (C036–C041)
- C036 — Job needed to develop talents  
- C037 — Humiliating to get money without work  
- C038 — People who don’t work turn lazy  
- C039 — Work is a duty to society  
- C041 — Work comes first even if less spare time  

## Values & Wellbeing
- Y002 — Post-materialist 4-item index  
- Y003 — Autonomy Index  
- A170 — Life satisfaction  
- A173 — Freedom of choice and control (Agency)  
"""

def get_schema_dict():
    """Parses the markdown table into a dictionary keyed by Variable name."""
    lines = variable_info_md.strip().split('\n')
    
    # Find table start
    table_lines = []
    in_table = False
    for line in lines:
        if line.strip().startswith('| Variable |'):
            in_table = True
        if in_table:
            if line.strip() == '' or line.startswith('#'):
                break
            table_lines.append(line)
            
    if not table_lines:
        return {}

    # Parse headers
    headers = [h.strip() for h in table_lines[0].split('|') if h.strip()]
    
    schema = {}
    # Skip header and separator
    for line in table_lines[2:]:
        if not line.strip(): continue
        row = [cell.strip() for cell in line.split('|') if cell.strip()]
        if len(row) >= len(headers):
            # Create a dict for this row
            row_dict = {headers[i]: row[i] for i in range(len(headers))}
            # Key by Variable name
            var_name = row_dict.get('Variable')
            if var_name:
                schema[var_name] = row_dict
                
    return schema

def get_item_descriptions():
    """Parses the item-level descriptions into a dictionary {ItemCode: Description}."""
    lines = variable_info_md.strip().split('\n')
    
    items = {}
    import re
    # Regex to match "- CODE — Description"
    # Handles codes like G006, E069_01
    pattern = re.compile(r'-\s+([A-Z0-9_]+)\s+[—–-]\s+(.+)')
    
    for line in lines:
        line = line.strip()
        match = pattern.match(line)
        if match:
            code = match.group(1).strip()
            desc = match.group(2).strip()
            items[code] = desc
            
    return items


