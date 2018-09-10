# For loops

# case 1
# using list
print("For loop to traverse list")
list1 = [10,20,30,40,50]
for num in list1:
    print(num)
# try displaying in a single line

# case 2
# using string
print("For loop to traverse string")
str1 = "Hello"
for s in str1:
    print(s)
# try displaying in a single line

# case 3
# using dictionary
print("For loop to traverse dictionary")
dict1 = {"Name": "Guruaraj", "Age":24, "Salary":2300}
for d in dict1:
    print(d, end=',')       #Note this will print the keys
                   #same as dict1.keys()
    print(dict1[d], end=',')#print values
print('\n')    
# print keys       
print(dict1.keys())

# print values
print(dict1.values())

# case 4
# using set
print("For loop to traverse set")
set1 = {10,20,20,30,40}
for s in set1:
    print(s)

# Try using Tuple
