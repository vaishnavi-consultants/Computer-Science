# functions
# Pass by object referenc
# Notes:
# ------
# passing a list to a function
# Summary:
# --------
# In Python, values are passed to functions by object references.
# If the object is immutable, the modified value is not available outside
# the function and if the object is mutable, its modified version is available
# outside the function.
# Please observe the id value before and after function call.

def modify(lst):
    """ to add a new element to list """
    lst.append(9)
    print(lst, id(lst))

#call modify() and pass lst
lst = [1,2,3,4]
print("list and id before calling modify function\n", lst, id(lst))
print("After modification")
modify(lst)
print(lst, id(lst))
print("Please note the id value of list before and after modification")



