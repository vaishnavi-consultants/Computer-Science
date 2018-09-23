# Sequences

#   str
print("*" * 15)
print("Case1: String representation")
print("*" * 15)
# str - String representation
str1 = "Welcome to Python Training"
print(str1)
# Welcome to Python Training

str2 = 'Welcome to Python Training'
print(str2)
# Welcome to Python Training

str3 = ''' This line spans over
multiline'''
print(str3)
#  This line spans over
# multiline

str4 = """ This line also spans
over multiline"""
print(str4)
#  This line also spans
# over multiline

print("*" * 15)
print("Case 2: String Iteration")
print("*" * 15)
SampleS = "Welcome"
# Iterating thorugh the string and printing
for c in SampleS:
    print(c, end=' ')

print("")

print("*" * 15)
print("Case 3: in operator")
print("*" * 15)
# in operator
if "k" in SampleS:
    print("k found in SampleS")
else:
    print("k not found in SampleS")

# in operator
if "W" in SampleS:
    print("W found in SampleS")
else:
    print("W not found in SampleS")

# Substring search
print("searching 'come' in Welcome")
print('come' in SampleS)
print("*" * 15)
print("Case 4: slice/indexing operator")
print("*" * 15)
# str - slicing
str1 = "Welcome"
str2 = "Python"
print(str1[0])
# W

print(str1[3:7])
# come

print(str1[3:])
# come

print(str1[-1])
# e

print(str1[:-1])
# Welcom
print("*" * 15)
print("Case 5: Repetition")
print("*" * 15)

print(str1 * 2)
#WelcomeWelcome
print("*" * 15)
print("Case 6: Concatenation")
print("*" * 15)
print(str1 + str2)
# WelcomePython
