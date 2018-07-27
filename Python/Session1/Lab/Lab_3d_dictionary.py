# Mapping Types
# Properties
# 1. A map represents a group of elements in the form of key value pairs so that when the key is given,
#    we can retrieve the value associated with it.
# 2. The dict datatype is an example for a map.
# 3. The ‘dict’ represents a ‘dictionary’ that contains pairs of elements such that the first element
#    represents the key and the next one becomes its value.
# 4. The key and its value should be separated by a colon (:) and every pair should be separated by a comma.
# 5. All the elements should be enclosed inside curly brackets {}.
# 6. you can use any immutable type as index.

# Dictionary creation - Method1
personrec = {}
personrec['name'] = 'naveen'
personrec['age'] = '35'

# print the dictionary
print(personrec)
# {'name': 'naveen', 'age': '35'}

# Dictionary creation - Method2
student = {'name': 'Rajeev','class':'4','course':'computers'}

# print the dictionary
print(student)
# {'name': 'Rajeev', 'class': '4', 'course': 'computers'}

# printing keys using keys() and for loop.
print("Getting keys using keys() function")
print(student.keys())
# Result
# ------
# Getting keys using keys() function
# dict_keys(['name', 'class', 'course'])

print("Getting keys using for loop")
for stu  in student:
    print(stu)

# Result
# ------
# Getting keys using for loop
# name
# class
# course    

# Retrival
print(student['name'])
# Rajeev

# update
num = int(student['class']) + 1
student['class'] = str(num)
print(student)
# {'name': 'Rajeev', 'class': '5', 'course': 'computers'}

# delete field
del student['course']
print(student)
#{'name': 'Rajeev', 'class': '5'}

print(student.keys())
# dict_keys(['name', 'class'])

print(student.values())
# dict_values(['Rajeev', '5'])
