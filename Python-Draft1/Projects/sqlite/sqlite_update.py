# code for update operation
import sqlite3
from sqlite_fetch import sqlite3_fetch_rec

# python sqlite.py Update Accounts employee "SET salary = '50000' where emp_id=2"

def sqlite3_update_rec(dbname, tablename, condi):
   
   # database name to be passed as parameter
   db_name = dbname+".db"
   conn = sqlite3.connect(db_name)
 
   # update the student record
   sql_command = """UPDATE """ + tablename + """ """ + condi
   conn.execute(sql_command)
   #conn.execute("UPDATE emp SET fname = 'Sams' where staff_number='1'")
   conn.commit() 
   print ("Total number of rows updated :", conn.total_changes)

   # fetch and display the db records
   sqlite3_fetch_rec(dbname, tablename)    

   # close the connection 
   conn.close()
