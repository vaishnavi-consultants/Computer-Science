# Converting List to other datatype

# List of Strings to a String
listOfStrings0 = ['One', 'Two', 'Three']
print("listOfStrings",listOfStrings0)
strOfStrings = ''.join(listOfStrings0)
print(strOfStrings)

# List Of Integers to a String
listOfNumbers1 = [1, 2, 3]
print("listOfNumbers", listOfNumbers1)
strOfNumbers = ''.join(str(n) for n in listOfNumbers1)
print(strOfNumbers)

# Pass your list to `tuple()`
listOfStrings2 = ['One', 'Two', 'Three']
print(tuple(listOfStrings2))

# Transform your list into a set
listOfStrings3 = ['One', 'Two', 'Three']
print(set(listOfStrings3))


# Result
# listOfStrings ['One', 'Two', 'Three']
# OneTwoThree
# listOfNumbers [1, 2, 3]
# 123
# ('One', 'Two', 'Three')
# {'One', 'Two', 'Three'}
