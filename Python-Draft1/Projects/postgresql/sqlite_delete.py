# code for delete operation

import psycopg2
from sqlite_fetch import sqlite3_fetch_rec

# python sqlite.py Delete Accounts employee "emp_id=1"

def sqlite3_delete_rec(dbname, tablename, condi):
 
   # database name to be passed as parameter
   db_name = dbname+".db"
   conn = psycopg2.connect("dbname='database1' user='postgres' password='Athu03#' host='localhost' port='5432'")

   # cursor 
   crsr = conn.cursor()  
 
   # delete student record from database
   sql_command = """DELETE from """ + tablename + """ where """+ condi
   crsr.execute(sql_command)
   conn.commit()
   
   # fetch and display the db records
   sqlite3_fetch_rec(dbname, tablename)
   
   # close the connection
   conn.close()
