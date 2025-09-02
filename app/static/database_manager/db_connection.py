#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : db_connection.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
import sqlite3

#-----------------------------------------------------------------------------------------------#
def create_db_connection():
    # DB Path
    CABTEK_WEB_APPS_DB_PATH = f"\\\\MANAGER1\\SharedDatabase\\CabTek Web Apps Database\\cabtek_web_apps.db"
    connection = sqlite3.connect(CABTEK_WEB_APPS_DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

#-----------------------------------------------------------------------------------------------#

def close_db_connection_on_error(connection):
    try:
        if connection:
                connection.rollback()  # Rollback any pending changes
                connection.close()
    except:
        pass
    
#-----------------------------------------------------------------------------------------------#