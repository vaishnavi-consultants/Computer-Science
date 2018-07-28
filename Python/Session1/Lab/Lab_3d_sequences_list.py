# Sequences

# List datatype
# Properties
# 1. A list is an ordered set of values, where each value
#    is identied by an index.
# 2. The values that make up a list are called its elements.
# 3. Lists are similar to strings, which are ordered sets of characters,
#    except that the elements of a list can have any type.

# list Values
list1 = [10, 20, 30, 40]
print("list1 ", list1)
list2 = ["Bangalore", "Delhi", "Tamilnadu"]
print("list2 ", list2)
# Nested List
list3 = ["Hello", 2.0, 5, [10, 20, "Kerala", -20, 2.99]] 
print("list3 ", list3)

# Result
# ------
# list1  [10, 20, 30, 40]
# list2  ['Bangalore', 'Delhi', 'Tamilnadu']
# list3  ['Hello', 2.0, 5, [10, 20, 'Kerala', -20, 2.99]]

# Indexing
print(list1[2])
# printing nested list and its value
print(list3[3])
print(list3[3][0])
print(list2[-2])

# Result
# ------
# 30
# [10, 20, 'Kerala', -20, 2.99]
# 10

# Slicing
print(list3[1:3])

print(list3[3][1:3])

# Result
# ------
# [2.0, 5]
# [20, 'Kerala']

# Repetition
print( list1 * 2)

# concatenation
print (list1 +  list2)

# Result
# ------
# [10, 20, 30, 40, 10, 20, 30, 40]
# [10, 20, 30, 40, 'Bangalore', 'Delhi', 'Tamilnadu']

# Append
print("Appending to list1 50")
print('Current list1 items')
print(list1)
print("Append 50")
list1.append(50)
print("Ater appending")
print(list1)

# Result
# Appending to list1 50
# Current list1 items
# [10, 20, 30, 40]
# Append 50
# Ater appending
# [10, 20, 30, 40, 50]
