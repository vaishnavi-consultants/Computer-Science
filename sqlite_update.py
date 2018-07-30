# code for update operation
import sqlite3
 
# database name to be passed as parameter
conn = sqlite3.connect('myTable.db')
 
# update the student record
conn.execute("UPDATE emp SET fname = 'Sams' where staff_number='1'")
conn.commit()
 
print ("Total number of rows updated :", conn.total_changes)
 
cursor = conn.execute("SELECT * FROM emp")
for row in cursor:
   print(row)
 
conn.close()
