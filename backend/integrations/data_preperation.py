import pandas as pd
import numpy as np
import sqlite3
from sql_helper import sql_handler

#Data
input_data = pd.read_excel('backend\\integrations\\files\\TFA_annon_GPT_dataset.xlsx')
input_data['PostingDate'] = pd.to_datetime(input_data['PostingDate'], errors='coerce').dt.strftime('%Y-%m-%d')
print(input_data.columns)
print(input_data['PostingDate'].dtype)

metadata_xlsx = pd.read_excel('backend\\integrations\\files\\GPT_TMD.xlsx')
tables = metadata_xlsx['TableName'].unique()
rows = []
for table in tables:
    rows.append((table, metadata_xlsx[metadata_xlsx['TableName'] == table]['ColumnName'].values.tolist()))

print("(<TableName>, [<Column1>, <Column2>, ...]): ", rows)

dfs = {}
print("All columns in data: ", input_data.columns.values.tolist())
for row in rows:
    columns_to_split_existing = [col for col in row[1] if col in input_data.columns]
    if len(columns_to_split_existing) > 0:
        print('Column that exists in the metadata table: ', row[0], columns_to_split_existing)
        dfs[row[0]] = input_data[columns_to_split_existing]

for idx, table_name in enumerate(list(dfs.keys())):
    print(f'Iteration {idx}')
    #Column list:
    column_list = dfs[table_name].columns.values.tolist()
    
    #Unique items
    print('Unique items: ', set(dfs[table_name].dtypes.values.tolist()))

    #Find Data Types:
    _dict = {'int64': 'int', 'object': 'varchar(250)', 'datetime64[ns]': 'varchar(30)', 'float64': 'real'}
    types_list = []
    for key in dfs[table_name].dtypes.values.tolist():
        if str(key) in _dict:
            types_list.append(_dict[str(key)])

    column_list_with_types = [f"{col} {type}" for col, type in zip(column_list, types_list)]
    print(column_list_with_types)

    #DB Upload
    #db_upload(dfs[table_name], column_list, column_list_with_types, table_name)    

#Create SQL script:
#prompt = "What is the lowest transaction amount in local currency?"
#response = nlp_to_sql_translator(f"This is my metadata tabel: {metadata_str}. Please create a SQL query for this request {prompt}")
#print(response)
    
#sql_script = response[0].replace('\n', ' ')[3:]
#print(sql_script)
#output_data = db_execute_sql(database_name='PyAutomate', server_name='DK2CPHDM01\DM01', sql_script=sql_script)
#print(output_data[0][0])