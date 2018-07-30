# code for delete operation
import sqlite3
from sqlite_fetch import sqlite3_fetch_rec

# python sqlite.py Delete Accounts employee "emp_id=1"

def sqlite3_delete_rec(dbname, tablename, condi):
 
   # database name to be passed as parameter
   db_name = dbname+".db"
   conn = sqlite3.connect(db_name)
 
   # delete student record from database
   sql_command = """DELETE from """ + tablename + """ where """+ condi
   conn.execute(sql_command)
   conn.commit()
   print ("Total number of rows deleted :", conn.total_changes)

   # fetch and display the db records
   sqlite3_fetch_rec(dbname, tablename)
   
   # close the connection
   conn.close()
