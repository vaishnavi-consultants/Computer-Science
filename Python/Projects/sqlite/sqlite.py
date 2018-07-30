# sqlite
# This is main program which parses the command line arguments
# executes the query:
# 1. Create database
# 2. Insert to database
# 3. Update the records
# 4. Delete the records

# Command line
# python sqlite.py <operation> <database> <tablename> <values>
# Example: python sqlite.py insert myDatabase.db emp "23, 'Guru'"

import sys
import argparse
from sqlite_create_db import sqlite3_create_db
from sqlite_insert import sqlite3_insert_rec
from sqlite_fetch import sqlite3_fetch_rec
from sqlite_delete import sqlite3_delete_rec

# Create an object of ArgumentParser class
parser = argparse.ArgumentParser(description='Sqlite Database')

# Method 2 - Retriving command line arguments
# Add arguments
parser.add_argument("op", type=str, help="Operation to perform")
parser.add_argument("db", type=str, help="Database name")
parser.add_argument("tbl", type=str, help="Database Table")
parser.add_argument("rec", type=str, help="Record to insert")

args = parser.parse_args()
print('Priting vlaues using parser.parse_args')
print('op=',args.op, end='\t')
print('db=',args.db, end='\t')
print('rec=',args.rec)

if args.op == "Insert":
    print("Inserting new record in to database")
    sqlite3_insert_rec(args.db, args.tbl, args.rec)
elif args.op == "Update":
    sqlite3_update_rec()
    # conn.execute("UPDATE Student SET name = 'Sam' where unix='B113059'")
elif args.op == "Delete":
    # conn.execute("DELETE from Student where unix='B113058'")
    sqlite3_delete_rec(args.db, args.tbl, args.rec)
elif args.op == "Fetch":
    sqlite3_fetch_rec(args.db, args.tbl)
elif args.op == "Create":
    # Creating new db
    print("Creating new db by name",args.db)
    print("Creating new table",args.rec, "in", args.db, "database")
    sqlite3_create_db(args.db, args.tbl)
else:
    print("Invalid option")
    print("Syntax: python sqlite.py <operation> <database> <tablename> <values>")
    
# Method 1 - Retriving command line arguments
# n = len(sys.argv)
# argument list containing arguments
# args = sys.argv

# print('No of command line arguments=', n)
# print('The args are: ', args)
# print('The args one by one')
# for argument in args:
#    print(argument)


# PROGRAM 2

# Data input by User
# code for executing query using input data
# import sqlite3
 
# creates a database in RAM
# con = sqlite3.connect(":memory:")
# cur = con.cursor()
# cur.execute("create table person (name, age, id)")
 
# print ("Enter 5 students names:")
# who = [raw_input() for i in range(5)]
# print ("Enter their ages respectively:")
# age = [int(raw_input()) for i in range(5)]
# print ("Enter their ids respectively:")
# p_id = [int(raw_input()) for i in range(5)]
# n = len(who)
 
# for i in range(n):
 
    # This is the q-mark style:
    # cur.execute("insert into person values (?, ?, ?)", (who[i], age[i], p_id[i]))
 
    # And this is the named style:
    # cur.execute("select * from person")
 
    # Fetches all entries from table
    # print cur.fetchall()
