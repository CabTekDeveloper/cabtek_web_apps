#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : tbl_user_roles.py
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
tbl_user_roles ="tbl_user_roles"
fn_user_id = "user_id"
fn_role_id  = "role_id"
#-----------------------------------------------------------------------------------------------#

def create_tbl_user_roles():
    try:
        sql = f''' CREATE TABLE IF NOT EXISTS {tbl_user_roles} (
                {fn_user_id} Integer NOT NULL,
                {fn_role_id} Integer NOT NULL,
                UNIQUE ({fn_user_id}, {fn_role_id})
                
            )'''
        connection = create_db_connection()
        connection.execute(sql)
        connection.close()
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        
#-----------------------------------------------------------------------------------------------#

def insert_into_tbl_user_roles(user_id, role_id):
    try:
        connection = create_db_connection()
        cursor = connection.cursor()
        sql = f''' INSERT INTO {tbl_user_roles} ({fn_user_id}, {fn_role_id}) VALUES (?,?) '''
        cursor.execute(sql, [user_id, role_id])
        connection.commit()
        cursor.close()
        connection.close()
        
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')

#-----------------------------------------------------------------------------------------------#

def get_user_role_ids_by_user_id(user_id):
    db_data = []
    try:
        sql = f''' SELECT * FROM {tbl_user_roles} WHERE {fn_user_id} = ?'''
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(sql,[user_id])
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        for row in rows:
            for key in row.keys():
                if key == fn_role_id:
                    db_data.append(row[key])

        return db_data
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return []
