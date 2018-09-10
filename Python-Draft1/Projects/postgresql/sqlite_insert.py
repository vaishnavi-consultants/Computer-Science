# Python code to demonstrate table creation and 
# insertions with SQL
 
# importing module
# python sqlite.py Insert Accounts employee "3, 'Maha', '240000', 'M', 'Software'"

import psycopg2

def sqlite3_insert_rec(dbname, tablename, rec):
 
    # connecting to the database
    db_name = dbname+".db"
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Athu03#' host='localhost' port='5432'")
 
    # cursor 
    crsr = conn.cursor()   
 
    # SQL command to insert the data in the table
    sql_command = """INSERT INTO """ + tablename + """ VALUES (""" + rec + """);"""    
    crsr.execute(sql_command)
 
    # To save the changes in the files. Never skip this. 
    # If we skip this, nothing will be saved in the database.
    conn.commit()
 
    # close the connection
    conn.close()
