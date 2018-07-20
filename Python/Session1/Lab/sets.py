# Sets

# Properties
# 1. A set is an unordered collection of elements.
# 2. The order of elements is not maintained in the sets.
# 3. It means the elements may not appear in the same order as they are entered into the set.
# 4. A set does not accept duplicate elements.
# 5. To create a set, we should enter the elements separated by commas inside curly braces {}.

# There are two sub types in sets:
#     set datatype
#     frozenset datatype

set1 = {10, 20, 30, 40, 50, 20, 10}
# print set
print(set1)

set2 = set("hello")
# print set
print(set2)

# convert list in to set using 'set'function
list1 = [1,3,6,7,8]
s = set(list1)
print(s)

# update
list3 = {10,20,40,50}
list3.update([100,200])
print(list3)

# remove
list3.remove(10)
print(list3)

#

# Result
# ------
# {40, 10, 50, 20, 30}
# {'e', 'l', 'o', 'h'}
# {1, 3, 6, 7, 8}
# {100, 40, 200, 10, 50, 20}
# {100, 40, 200, 50, 20}

# indexing and slicing not supported
# ----------------------------------
# Shell example
# >>> set1 = {1,2,40,50,60,20}
# >>> set1[3]
# Traceback (most recent call last):
#   File "<pyshell#104>", line 1, in <module>
#    set1[3]
# TypeError: 'set' object does not support indexing

# Frozen set - We can no modify the set.
# --------------------------------------
# >>> fs = frozenset(set1)
# >>> print(fs)
# frozenset({50, 100, 20, 40, 200})

# Error 1
# -------
# >>> fs[2] = 500
#Traceback (most recent call last):
#  File "<pyshell#114>", line 1, in <module>
#    fs[2] = 500
#TypeError: 'frozenset' object does not support item assignment
 
# Error 2
# -------
# >>> fs.update([700,800])
# Traceback (most recent call last):
#  File "<pyshell#117>", line 1, in <module>
#    fs.update([700,800])
#AttributeError: 'frozenset' object has no attribute 'update'

# Error 3
# -------
# >>> fs.remove(200)
# Traceback (most recent call last):
#   File "<pyshell#119>", line 1, in <module>
#    fs.remove(200)
# AttributeError: 'frozenset' object has no attribute 'remove'




