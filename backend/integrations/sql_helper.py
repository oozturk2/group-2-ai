import sqlite3
import numpy as pd
import pandas as pd

class sql_handler:
    def __init__(self):
        self.con = sqlite3.connect('backend\\integrations\\sql.db')
        self.cursor = self.con.cursor()
   
    def read_table_from_sql(self, table_name):
        df = pd.read_sql(f"SELECT * FROM {table_name};", self.con)
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
        sql = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
        self.cursor.execute(sql)
        table_exists = self.cursor.fetchone()
        return True if table_exists else False
    
    def _commit(self):
        self.con.commit()

def db_upload(df, col_list, col_list_with_types, table_name, ignore_into=False):
    db_obj  = sql_handler()
    val_list = df.replace(np.nan, None, regex=True).values.tolist()

    #Create Table:
    if not db_obj.table_does_exist(f'{table_name}'):
        #Table does not exist. Create one:
        db_obj.create_table_in_sql(f'{table_name}', col_list_with_types)

    db_obj.upload_to_sql(f'{table_name}', col_list, val_list, ignore_into)

def db_read(table_name):
    db_obj  = sql_handler()
    return db_obj.read_table_from_sql(table_name)

def db_create(table_name, col_list_with_types):
    db_obj = sql_handler()
    if not db_obj.table_does_exist(table_name):
        return db_obj.create_table_in_sql(table_name, col_list_with_types)
    
def db_execute_sql(sql_script):
    db_obj = sql_handler()
    db_obj.cursor.execute(sql_script)
    rows = db_obj.cursor.fetchall()
    return rows