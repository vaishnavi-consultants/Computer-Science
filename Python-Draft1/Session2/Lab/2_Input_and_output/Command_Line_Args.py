#to display command line args.

# Note: This module provides access to some variables used or maintained
#       by the interpreter and to functions that interact strongly with the interpreter.
#       It is always available.
import sys

n = len(sys.argv) #n is the number of arguments
args = sys.argv #args list contains arguments
print('No. of command line args=', n)
print('The args are:', args)
print('The args one by one:')

for a in args:
    print(a)


# Result
# ------
# C:\Users\harig\Documents\Personal\Python\Session2\Lab>python Lab_5c_Command_Line_Args.py 10 30 "Gururaj"
# No. of command line args= 4
# The args are: ['Lab_5c_Command_Line_Args.py', '10', '30', 'Gururaj']
# The args one by one:
# Lab_5c_Command_Line_Args.py
# 10
# 30
# Gururaj

# Program to TRY
# Add two number. Pass the numbers as command line arguments and add them. Display them.

# Program to TRY
# Can you extract '10', '20' and 'Gururaj' into a new list.?
