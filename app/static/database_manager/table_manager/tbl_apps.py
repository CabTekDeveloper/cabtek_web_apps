#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : tbl_apps.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
import inspect
import sys
import inspect
import pathlib
#-----------------------------------------------------------------------------------------------#
def get_cwd():
    cwd = str(pathlib.Path(__file__)).split("\\")[:-1]
    return "\\".join(cwd)
#-----------------------------------------------------------------------------------------------#
# Set path to current direcotry. This will help in importing modules.
# sys.path.append(get_cwd())

#-----------------------------------------------------------------------------------------------#

from  app.static.database_manager.db_connection import *

#-----------------------------------------------------------------------------------------------#
tbl_apps ="tbl_apps"
fn_name = "name"
#-----------------------------------------------------------------------------------------------#

def create_tbl_apps():
    sql = f''' CREATE TABLE IF NOT EXISTS {tbl_apps} (
            id Integer PRIMARY KEY AUTOINCREMENT,
            {fn_name} TEXT NOT NULL UNIQUE
        )'''
    connection = create_db_connection()
    connection.execute(sql)
    connection.close()
    
#-----------------------------------------------------------------------------------------------#

def insert_into_tbl_user_types(name):
    try:
        connection = create_db_connection()
        cursor = connection.cursor()
        sql = f''' INSERT INTO {tbl_apps} ({fn_name}) VALUES (?) '''
        cursor.execute(sql, [name])
        connection.commit()
        cursor.close()
        connection.close()
        
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        
#-----------------------------------------------------------------------------------------------#

def get_apps():
    data_db = []
    try:
        sql = f''' SELECT * FROM {tbl_apps} ORDER BY name COLLATE NOCASE ASC'''
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        for row in rows:
            data_db.append({key: row[key] for key in row.keys()})
        return data_db
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return []

#-----------------------------------------------------------------------------------------------#

