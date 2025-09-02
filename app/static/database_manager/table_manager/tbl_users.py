#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : tbl_users.py
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
fn_id           = "id"
tbl_users       ="tbl_users"
fn_name         = "name"
fn_user_name    = "user_name"
fn_password     = "password"
fn_email_id     = "email_id"
fn_mobile_no    = "mobile_no"
fn_phone_no     = "phone_no"
#-----------------------------------------------------------------------------------------------#

# phone/mobile no are stored as TEXT to allow spacings in between , ex:- "02 6284 4583"
def create_tbl_users():
    sql = f''' CREATE TABLE IF NOT EXISTS {tbl_users} (
            {fn_id} Integer PRIMARY KEY AUTOINCREMENT,
            {fn_name} TEXT NOT NULL,
            {fn_user_name} TEXT NOT NULL UNIQUE,
            {fn_email_id} TEXT NOT NULL,
            {fn_password} TEXT NOT NULL,
            {fn_mobile_no} TEXT,
            {fn_phone_no} TEXT
        )'''
    connection = create_db_connection()
    connection.execute(sql)
    connection.close()

#-----------------------------------------------------------------------------------------------#
    
def insert_into_tbl_users(name, user_name,  password, email_id,  mobile_no, phone_no):
    try:
        user_name = user_name.strip().lower()
        email_id = email_id.strip().lower()
        mobile_no = mobile_no.strip().lower()
        phone_no = phone_no.strip()
        
        connection = create_db_connection()
        cursor = connection.cursor()
        sql = f''' INSERT INTO {tbl_users} ({fn_name}, {fn_user_name}, {fn_password}, {fn_email_id},  {fn_mobile_no}, {fn_phone_no})   VALUES (?,?,?,?,?,?) '''
        cursor.execute(sql, [name, user_name, password, email_id, mobile_no, phone_no])
        connection.commit()
        cursor.close()
        connection.close()

    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        pass

#-----------------------------------------------------------------------------------------------#

def get_users():
    db_data = []
    try:
        sql = f''' SELECT * FROM {tbl_users} ORDER BY {fn_name} COLLATE NOCASE ASC '''
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        for row in rows:
            db_data.append({key: row[key] for key in row.keys()})

        return db_data
    except Exception as ex:
        close_db_connection_on_error(connection)
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return []
    
#-----------------------------------------------------------------------------------------------#
def get_user_info_by_id(id):
    data_db = {}
    try:
        sql = f' SELECT * FROM {tbl_users} WHERE {fn_id} = ? '
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
#-----------------------------------------------------------------------------------------------#

