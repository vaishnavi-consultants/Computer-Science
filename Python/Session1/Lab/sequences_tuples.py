# Sequences

# List datatype
# Properties
# 1. A tuple is similar to a list.
# 2. A tuple contains a group of elements which can be of different types.
# 3. The elements in the tuple are separated by commas and enclosed in parentheses ().
# 4. Whereas the list elements can be modified, it is not possible to modify the tuple elements.
#    That means a tuple can be treated as a read-only list.

tuple1 = (100, -20, 15.5, 'Gururaj', "Naveen", [10,20,30],("name","age"))

# print tuple
print("Tuple values")
for i in tuple1:
    print(i)

# Result
# ------
# Tuple values
# 100
# -20
# 15.5
# Gururaj
# Naveen
# [10, 20, 30]
# ('name', 'age')

print(tuple1[0])

print(tuple1[1:4])

print(tuple1[-4])

print(tuple1 * 2)

# Result
# ------

# 100
# (-20, 15.5, 'Gururaj')
# Gururaj
# (100, -20, 15.5, 'Gururaj', 'Naveen', [10, 20, 30], ('name', 'age'), 100, -20, 15.5, 'Gururaj', 'Naveen', [10, 20, 30], ('name', 'age'))




