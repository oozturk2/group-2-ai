import pandas as pd
import numpy as np
import mysql.connector as my
import pyodbc
 
class Sql:
    def __init__(self, database_name, server_name):
        self.database = database_name
        self.server = server_name
       
        self.con_str = ("Driver={ODBC Driver 17 for SQL Server};"
                    f"Database={database_name};"
                    f"Server={server_name};"
                    "Trusted_Connection=yes;")
       
        self.con = pyodbc.connect(self.con_str)
        self.cursor = self.con.cursor()
 
    def read_table_from_sql(self, table_name):
        df = pd.read_sql(f"SELECT * FROM dbo.{table_name};", self.con)
        self._commit()
        return df
   
    def create_table_in_sql(self, table_name, col_list_with_types):
        col_string = ', '.join(col_list_with_types)
        self.cursor.execute(f"CREATE TABLE {table_name} ({col_string})")
        self._commit()
   
    def upload_to_sql(self, table_name, col_list, val_list, ignore_into):
        col_string = ', '.join(col_list)
        str_for = '?, ' * len(col_list)
        if ignore_into == True:
            sql = f"INSERT IGNORE INTO {table_name} ({col_string}) VALUES ({str_for[:-2]})"
        else:
            sql = f"INSERT INTO {table_name} ({col_string}) VALUES ({str_for[:-2]})"
        self.cursor.executemany(sql, val_list)              
        self._commit()
 
    def table_does_exist(self, table_name):
        sql = f"SELECT * FROM information_schema.tables WHERE table_name = '{table_name}';"
        self.cursor.execute(sql)
        table_exists = self.cursor.fetchone()
        return True if table_exists else False
   
    def _commit(self):
        self.con.commit()
 
def db_upload(df, col_list, col_list_with_types, table_name, database_name, server_name, ignore_into=False):
    db_obj  = sql_handler(database_name, server_name)
    val_list = df.replace(np.nan, None, regex=True).values.tolist()
    #Create Table:
    if not db_obj.table_does_exist(f'{table_name}'):
        #Table does not exist. Create one:
        db_obj.create_table_in_sql(f'{table_name}', col_list_with_types)
    db_obj.upload_to_sql(f'{table_name}', col_list, val_list, ignore_into)
 
def db_read(table_name, database_name, server_name):
    db_obj  = sql_handler(database_name, server_name)
    return db_obj.read_table_from_sql(table_name)
 
def db_create(table_name, database_name, server_name, col_list_with_types):
    db_obj = sql_handler(database_name, server_name)
    if not db_obj.table_does_exist(table_name):
        return db_obj.create_table_in_sql(table_name, col_list_with_types)
    

