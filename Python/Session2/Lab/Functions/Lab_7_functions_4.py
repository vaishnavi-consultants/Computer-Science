# functions
# Pass by object referenc
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
# 4. In Python integers, floats, strings and tuples are immutable. 
#    That means their data cannot be modified. When we try to change their value, 
#    a new object is created with the modified value. Due to this, id(x) value will
#    change when we pass the data types.

print("*" * 15)    
print("Case 1: Pass integer to function and change it")
def update_function(x):
    print("id value of passed variable",id(x))
    x = x + 10
    print("id value after modifying the passed variable's value",id(x))
    return x

return1 = update_function(15)
print("retunr value", return1)

print("*" * 15)
print("Case 2: passing value and modifying it")
y = 15
print("id value of y before calling update_function")
print(id(y))
print("Calling update_function")
return1 = update_function(15)
print("Values returned", return1)
print("id value of returned value ",id(return1))
print("id value of y after calling update_function", id(y))
print("*" * 15)
