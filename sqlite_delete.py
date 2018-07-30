# code for delete operation
import sqlite3
 
# database name to be passed as parameter
conn = sqlite3.connect('myTable.db')
 
# delete student record from database
conn.execute("DELETE from emp where staff_number='1'")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)
 
cursor = conn.execute("SELECT * FROM emp")
for row in cursor:
   print (row)
 
conn.close()
