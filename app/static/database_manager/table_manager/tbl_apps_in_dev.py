#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : tbl_apps_in_dev.py
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
tbl_apps_in_dev ="tbl_apps_in_dev"
fn_app_id  = "app_id"
fn_user_id = "user_id"
#-----------------------------------------------------------------------------------------------#

def create_tbl_apps_in_dev():
    try:
        sql = f''' CREATE TABLE IF NOT EXISTS {tbl_apps_in_dev} (
                {fn_app_id} Integer NOT NULL UNIQUE,
                {fn_user_id} Integer NOT NULL
            )'''
        connection = create_db_connection()
        connection.execute(sql)
        connection.close()
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        
#-----------------------------------------------------------------------------------------------#

def insert_into_tbl_app_in_dev(app_id, user_id):
    try:
        connection = create_db_connection()
        cursor = connection.cursor()
        sql = f''' INSERT INTO {tbl_apps_in_dev} ({fn_app_id}, {fn_user_id}) VALUES (?,?) '''
        cursor.execute(sql, [app_id, user_id])
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return False
#-----------------------------------------------------------------------------------------------#

def get_user_id_developing_app_by_app_id(app_id):
    data_db = None
    try:
        sql = f' SELECT {fn_user_id} FROM {tbl_apps_in_dev} WHERE {fn_app_id} = ? '
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, [app_id])
        row = cursor.fetchone()
        cursor.close()
        connection.close()

        if row:
            data_db = {key: row[key] for key in row.keys()}['user_id']

        return data_db
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return None
    #-----------------------------------------------------------------------------------------------#

def remove_app_in_dev_by(app_id, user_id):
    try:
        sql = f' DELETE FROM {tbl_apps_in_dev} WHERE {fn_app_id} = ? AND {fn_user_id} = ? '
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, [app_id, user_id])
        connection.commit()
        connection.close()

        return True
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return False


#-----------------------------------------------------------------------------------------------#

def get_apps_in_dev():
    data_db = []
    try:
        sql = f' SELECT * FROM {tbl_apps_in_dev} '
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



