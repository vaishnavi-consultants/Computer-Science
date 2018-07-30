# Python code to demonstrate SQL to fetch data.
 
# importing the module
import sqlite3

def sqlite3_fetch_rec(dbname, tablename):
 
    # connect withe the myTable database
    db_name = dbname+".db"
    connection = sqlite3.connect(db_name)
 
    # cursor object
    crsr = connection.cursor()
 
    # execute the command to fetch all the data from the table emp
    crsr.execute("SELECT * FROM "+ tablename) 
 
    # store all the fetched data in the ans variable
    ans= crsr.fetchall() 
 
    # loop to print all the data
    for i in ans:
        print(i)
