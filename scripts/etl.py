import pandas as pd

# Importar configuraciones y funciones
from config import *
from utils import *

# Cargar datos
paths = setup_paths()

# Cargar datos
file = os.path.join(paths['data_raw'], 'global_oc_index.xlsx')

df_21 = pd.read_excel(file, sheet_name='2021_dataset')
df_23 = pd.read_excel(file, sheet_name='2023_dataset')

df_21.insert(3, 'year', 2021)
df_23.insert(3, 'year', 2023)

COLUMN_MAPPING = {
    'Continent': 'continent',
    'Region': 'region',
    'Country': 'country',
    'Criminality': 'criminality',
    'Criminal markets': 'criminal_markets',
    'Human trafficking': 'human_trafficking',
    'Human smuggling': 'human_smuggling',
    'Arms trafficking': 'arms_trafficking',
    'Flora crimes': 'flora_crimes',
    'Fauna crimes': 'fauna_crimes',
    'Non-renewable resource crimes': 'non_renewable_resource_crimes',
    'Heroin trade': 'heroin_trade',
    'Cocaine trade': 'cocaine_trade',
    'Cannabis trade': 'cannabis_trade',
    'Synthetic drug trade': 'synthetic_drug_trade',
    'Criminal actors': 'criminal_actors',
    'Mafia-style groups': 'mafia_groups',
    'Criminal networks': 'criminal_networks',
    'State-embedded actors': 'state_embedded_actors',
    'Foreign actors': 'foreign_actors',
    'Resilience': 'resilience',
    'Political leadership and governance': 'political_leadership_governance',
    'Government transparency and accountability': 'government_transparency_accountability',
    'International cooperation': 'international_cooperation',
    'National policies and laws': 'national_policies_laws',
    'Judicial system and detention': 'judicial_system_detention',
    'Law enforcement': 'law_enforcement',
    'Territorial integrity': 'territorial_integrity',
    'Anti-money laundering': 'anti_money_laundering',
    'Economic regulatory capacity': 'economic_regulatory_capacity',
    'Victim and witness support': 'victim_witness_support',
    'Prevention': 'prevention',
    'Non-state actors': 'non_state_actors',
    'Criminality avg,': 'criminality_avg',
    'Criminal markets avg,': 'criminal_markets_avg',
    'Cyber-dependent crimes': 'cyber_dependent_crimes',
    'Financial crimes': 'financial_crimes',
    'Trade in counterfeit goods': 'counterfeit_goods_trade',
    'Illicit trade in excisable goods': 'illicit_trade_excisable_goods',
    'Extortion and protection racketeering': 'extortion_protection_racketeering',
    'Criminal actors avg,': 'criminal_actors_avg',
    'Private sector actors': 'private_sector_actors',
    'Resilience avg,': 'resilience_avg',
    'year': 'year'
}

# Renombrar columnas en ambos DataFrames
df_21.rename(columns=COLUMN_MAPPING, inplace=True)
df_23.rename(columns=COLUMN_MAPPING, inplace=True)

# Concatenar los DataFrames
df = pd.concat([df_21, df_23], axis=0)

# Exportar datos procesados
df.to_csv(os.path.join(paths['data_processed'], 'data_processed.csv'), index=False)