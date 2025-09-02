#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Added by     : Wangchuk, 
# Dated added  : 21-05-2025
# BluePrint    : app  
# File         : alter_defs.py
#-----------------------------------------------------------------------------------------------------------------------------------------------------------#
# Set path to current direcotry



from  app.static.database_manager.db_connection import *
#-----------------------------------------------------------------------------------------------#
def drop_table(table_name):
    table_name = table_name.strip()
    connection = create_db_connection()
    cursor = connection.cursor()
    sql = f"DROP TABLE {table_name} ;"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()


#-----------------------------------------------------------------------------------------------#
def alter_delete_column(table_name, column_name):
    connection = create_db_connection()
    cursor = connection.cursor()
    sql = f"ALTER TABLE {table_name} DROP COLUMN {column_name};"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    
#-----------------------------------------------------------------------------------------------#
def alter_add_column(table_name, new_column_name, dataType):
    connection = create_db_connection()
    cursor = connection.cursor()
    sql = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {dataType};"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
# alter_add_column(table_name= "quotes_tableX", new_column_name= "company_id", dataType= "Integer")
#-----------------------------------------------------------------------------------------------#
def update_a_field(table_name, column_name, val):
    try:
        sql = f" UPDATE {table_name} SET {column_name} = ? "
        
        connection = create_db_connection()
        cursor = connection.cursor()
        cursor.execute(sql, [val])
        connection.commit()
        cursor.close()
        connection.close()
    except:
        pass
#-----------------------------------------------------------------------------------------------#
def alter_rename_column(table_name, old_name, new_name):
    connection = create_db_connection()
    cursor = connection.cursor()
    sql = f"ALTER TABLE {table_name} RENAME COLUMN {old_name} to {new_name};"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
# alter_rename_column(table_name= "quotes_tableXX", old_name = "company_id", new_name= "company_id")
#-----------------------------------------------------------------------------------------------#