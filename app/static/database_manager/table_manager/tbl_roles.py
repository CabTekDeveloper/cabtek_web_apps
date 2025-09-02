#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : tbl_roles.py
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
tbl_roles ="tbl_roles"
fn_id = "id"
fn_name = "name"
#-----------------------------------------------------------------------------------------------#
def create_tbl_roles():
    try:
        sql = f''' CREATE TABLE IF NOT EXISTS {tbl_roles} (
                {fn_id} Integer PRIMARY KEY AUTOINCREMENT,
                {fn_name} TEXT NOT NULL UNIQUE
            )'''
        connection = create_db_connection()
        connection.execute(sql)
        connection.close()
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
#-----------------------------------------------------------------------------------------------#

def insert_into_tbl_roles(name):
    try:
        connection = create_db_connection()
        cursor = connection.cursor()
        sql = f''' INSERT INTO {tbl_roles} ({fn_name}) VALUES (?) '''
        cursor.execute(sql, [name])
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
#-----------------------------------------------------------------------------------------------#

def get_role_info_by_id(id):
    data_db = {}
    try:
        sql = f' SELECT * FROM {tbl_roles} WHERE {fn_id} = ? '
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, [id])
        row = cursor.fetchone()
        cursor.close()
        connection.close()

        if row != None:
            data_db = {key: row[key] for key in row.keys()}

        return data_db
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return {}

