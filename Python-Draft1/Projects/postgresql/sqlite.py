#-------------------------------------------------------------------------- 
# sqlite3 - DB-API 2.0 interface for SQLite databases
# Documentation:
# SQLite is a C library that provides a lightweight disk-based database
# that doesn’t require a separate server process and allows accessing the
# database using a nonstandard variant of the SQL query language. Some
# applications can use SQLite for internal data storage.
# It’s also possible to prototype an application using SQLite and then port
# the code to a larger database such as PostgreSQL or Oracle.
#--------------------------------------------------------------------------
# Note: In this small project we study about
# -----
# 1. argparse - Parser for command-line options, arguments and sub-commands.
# 2. sqlite3.
# 3. functions - Defining functions, calling them, importing.
# 4. control statements.
# 
# This is main program which parses the command line arguments
# executes the query based on user input:
# 1. Create database
# 2. Insert to database
# 3. Update the records
# 4. Delete the records

# usage: sqlite.py [-h] op db tbl rec
# Note: op - operation ( Create, Delete, Insert, Update or Fetch )
#       db - Database name
#       tbl - Table in the database
#       rec - Record to insert. This is valid for Create.

import sys
# The argparse module:
# --------------------
# The argparse module makes it easy to write user-friendly command-line interfaces.
# The program defines what arguments it requires, and argparse will figure out how
# to parse those out of sys.argv.
# The argparse module also automatically generates help and
# usage messages and issues errors when users give the program invalid arguments.
import argparse

from sqlite_create_db import sqlite3_create_db
from sqlite_insert import sqlite3_insert_rec
from sqlite_fetch import sqlite3_fetch_rec
from sqlite_delete import sqlite3_delete_rec
from sqlite_update import sqlite3_update_rec

# Create an object of ArgumentParser class
parser = argparse.ArgumentParser(description='Sqlite Database')

# Method 1 - Retriving command line arguments
# n = len(sys.argv)
# argument list containing arguments
# args = sys.argv

# print('No of command line arguments=', n)
# print('The args are: ', args)
# print('The args one by one')
# for argument in args:
#    print(argument)

# Method 2 - Retriving command line arguments
# Add arguments
parser.add_argument("op", type=str, help="Operation to perform")
parser.add_argument("db", type=str, help="Database name")
parser.add_argument("tbl", type=str, help="Database Table")
parser.add_argument("rec", type=str, help="Record to insert/Conditions to check")

args = parser.parse_args()
print('op='+args.op, end='\t')
print('db='+args.db, end='\t')
print('tbl='+args.tbl, end='\t')
print('rec='+args.rec)

if args.op == "Insert":
    # Inserting new record in to db
    print("Inserting new record in to database")
    sqlite3_insert_rec(args.db, args.tbl, args.rec)
elif args.op == "Update":
    # Updating the existing record in the db
    print("Updating the existing record")
    sqlite3_update_rec(args.db, args.tbl, args.rec)
elif args.op == "Delete":
    # Deleting the existing record in the db
    print("Deleting the existing record")
    sqlite3_delete_rec(args.db, args.tbl, args.rec)
elif args.op == "Fetch":
    # Fetch the records in the db
    print("Fetch the records in database")
    sqlite3_fetch_rec(args.db, args.tbl)
elif args.op == "Create":
    # Creating new db
    print("Creating new db by name",args.db)
    print("Creating new table",args.rec, "in", args.db, "database")
    sqlite3_create_db(args.db, args.tbl)
else:
    print("Invalid option")
    print("Syntax: python sqlite.py <operation> <database> <tablename> <record>")

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
