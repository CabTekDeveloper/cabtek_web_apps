#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : db_manager.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# This module will import functions from differet table modules and return tailored data
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

import inspect

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

from app.static.database_manager.table_manager import tbl_users, tbl_roles, tbl_user_roles, tbl_apps, tbl_apps_in_dev

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# This function will
#   1. Get all users from tbl_users
#   2. Use id of user and get its role ids from tbl_user_roles 
#   3. Then, use the role id to get role info from tbl_roles and store in a new lis "user_roles"
#   4. Finally, add "user_roles" to all_users list

def validate_user(user_id, password):
    isValidUser = False
    try:
        user_info = tbl_users.get_user_info_by_id(user_id)
        if user_info:
            if user_info['password'] == password.strip():
                isValidUser = True     
                
        return isValidUser

    except Exception as ex:
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]') 
        return False


def get_single_user_by_id_db(user_id):
    data = {}
    try:
        data = tbl_users.get_user_info_by_id(user_id)
        if data:
            user_role_ids = tbl_user_roles.get_user_role_ids_by_user_id(user_id)
            data["user_roles"] = [tbl_roles.get_role_info_by_id(id) for id in user_role_ids]   
        return data
    except Exception as ex:
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]') 
        return {}

# print(get_user_info_db(2))

def get_all_users_db():
    data = []
    try:
        all_users = tbl_users.get_users()
        for user in all_users:
            user_role_ids = tbl_user_roles.get_user_role_ids_by_user_id(user['id'])
            user["user_roles"] = [tbl_roles.get_role_info_by_id(id) for id in user_role_ids]   
            data.append(user)
        return data
    except Exception as ex:
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]') 
        return []

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
def get_all_apps_db():
    data = []
    try:
        all_apps = tbl_apps.get_apps()
        for app in all_apps:
            user_info = {}
            user_id = tbl_apps_in_dev.get_user_id_developing_app_by_app_id(app['id'])
            if user_id:
                user_info = tbl_users.get_user_info_by_id(user_id)
            app['app_in_dev_by']  = user_info
            data.append(app)
        return data
    except Exception as ex:
        print(f'Error:"{ex}" [In function {inspect.stack()[0][3]}]')
        return []

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#


# print(tbl_apps_in_dev.get_apps_in_dev())