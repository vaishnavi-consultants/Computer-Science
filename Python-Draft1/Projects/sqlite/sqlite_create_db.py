# Python code to demonstrate table creation and 
# insertions with SQL

# TODO: pass databse fields through command line.
# TODO: create new database with different fileds.

# Syntax:  python sqlite.py create <database_name> <tablename>
# Example: python sqlite.py Create Accounts employee ""
 
# importing module
import sqlite3

def sqlite3_create_db(dbname, tablename):
    """ This function creates new database by name dbname"""
 
    # connecting to the database
    db_name = dbname+".db"
    connection = sqlite3.connect(db_name)
 
    # cursor 
    crsr = connection.cursor()

    # SQL command to create a table in the database
    sql_command = """CREATE TABLE """ + tablename + """ ( 
                    emp_id INTEGER PRIMARY KEY, 
                    emp_name VARCHAR(20), 
                    salary INTEGER, 
                    gender CHAR(1), 
                    department VARCHAR(10));"""
    
    print(sql_command)
 
    # execute the statement
    crsr.execute(sql_command) 

    # To save the changes in the files. Never skip this. 
    # If we skip this, nothing will be saved in the database.
    connection.commit()
 
    # close the connection
    connection.close()
