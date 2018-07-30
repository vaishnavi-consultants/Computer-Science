# sqlite
# This is main program which parses the command line arguments
# executes the query:
# 1. Create database
# 2. Insert to database
# 3. Update the records
# 4. Delete the records

# Command line
# python sqlite.py <operation> <database> <values>
# Example: python sqlite.py insert myDatabase.db "23, 'Guru'"

import sys
import argparse

# Create an object of ArgumentParser class
parser = argparse.ArgumentParser(description='Sqlite Database')

# Add arguments
parser.add_argument("op", type=str, help="Operation to perform")
parser.add_argument("db", type=str, help="Database name")
parser.add_argument("rec", type=str, help="Record to insert")

args = parser.parse_args()
print('Priting vlaues using parser.parse_args')
print('op', args.op)
print('db', args.db)
print('rec', args.rec)

# Method 1 - Retriving command line arguments
# n = len(sys.argv)
# argument list containing arguments
# args = sys.argv

# print('No of command line arguments=', n)
# print('The args are: ', args)
# print('The args one by one')
# for argument in args:
#    print(argument)
