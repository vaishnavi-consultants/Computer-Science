# Sequences

# bytearray datatype
# Properties:
# 1. The bytearray datatype represent a group of byte numbers in any
#   positive interer from 0 to 255(inclusive).
# 2. We can modify or edit any element in the bytearray type .
# 

# Create a list of byte numbers
numbers = [10,20,0,50,200]
# convert to list in to bytes type array
x = bytearray(numbers)
# print the values
print("Printing bytearray array\n")
for i in x:
    print(i)

print("Modify values and print")
x[2] = 100
for i in x:
    print(i)

# Result
# ------
# Printing bytearray array

# 10
# 20
# 0
# 50
# 200

# Modify values and print
# 10
# 20
# 100
# 50
# 200

# From shell
# ----------
# >>> numbers = [10, 20, 0, 50, 200]
# >>> num_to_bytearray = bytearray(numbers)
 
# >>> for i in num_to_bytearray:
#	print(i)

# 10
# 20
# 0
# 50
# 200

# Trying to modify the value  
# >>> num_to_bytearray[2] = 100

# >>> for i in num_to_bytearray:
#	print(i)
	
#10
#20
#100
#50
#200
 
