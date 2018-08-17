# functions
# Pass by object referenc
# Notes:
# ------
#passing a list to a function
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



