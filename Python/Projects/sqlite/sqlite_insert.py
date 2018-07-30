# Python code to demonstrate table creation and 
# insertions with SQL
 
# importing module
# python sqlite.py Insert Accounts employee "3, 'Sridevi', '240000', 'M', 'Software'"

import sqlite3

def sqlite3_insert_rec(dbname, tablename, rec):
 
    # connecting to the database
    db_name = dbname+".db"
    connection = sqlite3.connect(db_name)
 
    # cursor 
    crsr = connection.cursor()   
 
    # SQL command to insert the data in the table
    sql_command = """INSERT INTO """ + tablename + """ VALUES (""" + rec + """);"""    
    crsr.execute(sql_command)
 
    # To save the changes in the files. Never skip this. 
    # If we skip this, nothing will be saved in the database.
    connection.commit()
 
    # close the connection
    connection.close()
