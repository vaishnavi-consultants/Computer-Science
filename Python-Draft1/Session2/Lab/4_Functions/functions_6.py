# Functions
# Formal and Actual Arguments
# Notes:
# ------
# 1. In Python, the values are sent to functions by means of object references.
#    We know everything is considered as an object in Python.
#    All numbers are objects, strings are objects, and the datatypes like tuples, lists,
#    and dictionaries are also objects.
#
# 2. When we pass values like numbers, strings, tuples or lists to a function,
#    the references of these objects are passed to the function.
#
# 3. How objects are stored and tagged 

# Add two numbers
# Explains the concepts of Formal and Actual Arguments

def sum(a, b): #a, b are formal arguments
    c = a+b
    print(c)

#call the function
x=10; y=15
sum(x, y)       #x, y are actual argument

# Types of Actual Arguments
# -------------------------
#  Positional arguments
#  Keyword arguments
#  Default arguments
#  Variable length arguments

# Keyword arguments
# Keyword arguments are arguments that identify the parameters by their names.
print("Keyword arguments")
def employee(name, age):
    print("Name of employee "+name)
    print("Age of the employee %s is %d" %(name, age))

# Call the employee
employee(name="Gururaj", age=10)
employee(age=10, name="naveen")

# Result
# ------
# Keyword arguments
# Name of employee Gururaj
# Age of the employee Gururaj is 10
# Name of employee naveen
# Age of the employee naveen is 10

def complex(real, imag):
    print("%f + j %f"%(real, imag))

print("Using Keyword arguments")
complex(real=5, imag=10)
complex(**{'real':5, 'imag':10})  # Passed as a value in a dictionary.

# Positional Arguments
# 1. an argument that is not a keyword argument.
# 2. Positional arguments can appear at the beginning of an argument list and/or
#    be passed as elements of an iterable preceded by *

print("Using Positional arguments")
complex(3,5)
complex(*(3,5))

# Result
# ------
# Using Keyword arguments
# 5.000000 + j 10.000000
# 5.000000 + j 10.000000
# Using Positional arguments
# 3.000000 + j 5.000000
# 3.000000 + j 5.000000

# Using Default Arguments
# we can mention some default values for function parameters in the definition.
print("Using Default Argument, imag=100")
def complex(real, imag=100):
    print("%f + j %f"%(real, imag))

complex(5, 50)
complex(6)
complex(*(3,))
complex(real=300)
complex(**{'real':20})

# Result
# ------
# Using Default Argument, imag=100
# 5.000000 + j 50.000000
# 6.000000 + j 100.000000
# 3.000000 + j 100.000000
# 300.000000 + j 100.000000
# 20.000000 + j 100.000000

# Variable length arguments
# It can accept any number of arguments and * is used
# before the variable to denote it as variable argument.
# * is used to send non-keyworded variable length argument list to function.
# 
def add(fargs, *argv):
    print("fargs - first normal argument %d" %fargs)

    for i in argv:
        print("Another arg through *argv %d" %i)

print("Add two numbers")
add(2,3)    #  two numbers

print("Add three numbers")
add(2,3,4)  #  Three arguments

print("Add ten numbers")
add(1,2,3,4,5,6,7,8,9,10)   # Ten arguments

print("Only one argument")  # only one argument
add(1)

# Result
# Add two numbers
# fargs - first normal argument 2
# Another arg through *argv 3
# Add three numbers
# fargs - first normal argument 2
# Another arg through *argv 3
# Another arg through *argv 4
# Add ten numbers
# fargs - first normal argument 1
# Another arg through *argv 2
# Another arg through *argv 3
# Another arg through *argv 4
# Another arg through *argv 5
# Another arg through *argv 6
# Another arg through *argv 7
# Another arg through *argv 8
# Another arg through *argv 9
# Another arg through *argv 10

# using **kwargs
def test_args_kwargs(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)

# using with *args
print("Using *args")
args = ("two", 3,5)
test_args_kwargs(*args)

print("Using **kwargs")
# using with **kwargs
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)

# Result
# ------
# print("Using *args")
# arg1: two
# arg2: 3
# arg3: 5
# print("Using **kwargs")
# arg1: 5
# arg2: two
# arg3: 3
