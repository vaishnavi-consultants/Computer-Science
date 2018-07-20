# Sequences

# bytes datatype
# Properties:
# 1. The bytes datatype represent a group of byte numbers in any
#   positive interer from 0 to 255(inclusive).
# 2. We can not modify or edit any element in th ebytes type array.
# 

# Create a list of byte numbers
numbers = [10,20,0,50,200]
# convert to list in to bytes type array
x = bytes(numbers)
# print the values
print("Printing bytes array\n")
for i in x:
    print(i)

# Result
# Printing bytes array

# 10
# 20
# 0
# 50
# 200

# From shell

# >>> numbers = [10, 20, 0, 50, 200]
# >>> num_to_bytes = bytes(numbers)
 
# >>> for i in num_to_bytes:
	print(i)

# 10
# 20
# 0
# 50
# 200

# Trying to modify the value  
#>>> num_to_bytes[2] = 30
#Traceback (most recent call last):
#  File "<pyshell#76>", line 1, in <module>
#    num_to_bytes[2] = 30
#TypeError: 'bytes' object does not support item assignment
