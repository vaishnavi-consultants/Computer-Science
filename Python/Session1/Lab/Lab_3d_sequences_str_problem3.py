# This program explains basics operation on string
# startswith
# endswith
# find

text = 'yeah, but no, but yeah, but no, but yeah'

# exach match
print("Matching for exact match 'yeah'")
True_False = (text == 'yeah')
print(True_False)

# Match at start
print("Matching for sentence start with 'yeah'")
True_False = (text.startswith('yeah'))
print(True_False)

# Match at end
print("Matching for sentence end with 'no'")
True_False = (text.endswith('no'))
print(True_False)

# Search for the location fo the first occurance
print("Search for locaton of first occurance of 'no' word")
Location = (text.find('no'))
print(Location)

# Result

# Matching for exact match 'yeah'
# False
# Matching for sentence start with 'yeah'
# True
# Matching for sentence end with 'no'
# False
# Search for locaton of first occurance of 'no' word
# 10

# Transform List to Other data structure
print("Convert List to String")
# List of Strings to a String
listOfStrings = ['One', 'Two', 'Three']
print("listOfStrings",listOfStrings)
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)

# List Of Integers to a String
listOfNumbers = [1, 2, 3]
print("listOfNumbers", listOfNumbers)
strOfNumbers = ''.join(str(n) for n in listOfNumbers)
print(strOfNumbers)

# Result
# Convert List to String
# listOfStrings ['One', 'Two', 'Three']
# OneTwoThree
# listOfNumbers [1, 2, 3]
# 123
