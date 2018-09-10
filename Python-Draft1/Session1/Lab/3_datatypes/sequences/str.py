# Sequences

#   str
#   bytes
#   bytearray
#   list
#   tuple
#   range

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

print(str1 * 2)
#WelcomeWelcome

print(str1 + str2)
# WelcomePython
