import json 
import pandas as pd
import geopandas as gpd

gdf = gpd.read_file('populated_places.geojson', encoding = 'utf-8')

df = gdf.drop(columns = 'geometry')

df.to_csv('populated_places.csv', index = False)
print('Data extracted and saved to populated_places.csv')

df_villages = pd.read_csv('populated_places.csv')

df_villages_condition = (((df_villages['name'].str.strip() != '') | 
                         df_villages['name'].str.strip().notna() | 
                         df_villages['name'].str.strip().notnull()) &
                        df_villages['place'].str.lower().str.strip().isin(['village', 'town']))

df_villages = df_villages.loc[df_villages_condition, ['name', 'place','adm1_pcode','adm1_name','adm2_pcode', 'adm2_name','adm3_pcode', 'adm3_name']]

df_villages.rename(columns = {'name': 'village_name','adm1_pcode': 'region_pcode', 'adm1_name': 'region', 'adm2_pcode': 'division_pcode', 'adm2_name': 'division', 'adm3_pcode': 'sub_division_pcode', 'adm3_name': 'sub_division'}, inplace = True)

text_columns = ['village_name', 'place','region', 'division', 'sub_division']

for col in text_columns:
    if col in df_villages.columns:
        df_villages[col] = (
            df_villages[col].astype(str).str.encode('cp1252', errors='ignore').str.decode('utf-8', errors='ignore')
        )

df_villages.to_csv('cmr_villages.csv', index = False, encoding='utf-8-sig')

                        


