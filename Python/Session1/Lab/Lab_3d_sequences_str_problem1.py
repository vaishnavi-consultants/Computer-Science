# This explains the concept of
# a. using os module and its one of the function.
# b. List.

import os
filenames = os.listdir('.')
print("List of file name")
print(filenames)

# Print the name of files with extenstion .py
print("List of names end with .py")
for name in filenames:
    if name.endswith('.py'):
        print(name)
        

# Result

# List of file name
# ['Builtin_datatypes.txt', 'Lab_1c_add_two_int.py', 'Lab_3b_docstring.html', 'Lab_3b_docstring.py', 'Lab_3c_Types.txt', 'Lab_3c_variables.txt', 'Lab_3d_bool_datatype.txt', 'Lab_3d_converting_datatypes.txt', 'Lab_3d_convert_to_other_numbersystem.py', 'Lab_3d_dictionary.py', 'Lab_3d_ii_convert_to_decimal_number.py', 'Lab_3d_i_convert_to_decimal_number.py', 'Lab_3d_sequences_bytearray.py', 'Lab_3d_sequences_bytes.py', 'Lab_3d_sequences_list.py', 'Lab_3d_sequences_range.py', 'Lab_3d_sequences_str.py', 'Lab_3d_sequences_str_problem1.py', 'Lab_3d_sequences_tuples.py', 'Lab_3d_sets.py', 'Python(Final_Lists_Dictionary_Lab).docx', 'ReadMe.txt', '__pycache__']
# List of names end with .py
# Lab_1c_add_two_int.py
# Lab_3b_docstring.py
# Lab_3d_convert_to_other_numbersystem.py
# Lab_3d_dictionary.py
# Lab_3d_ii_convert_to_decimal_number.py
# Lab_3d_i_convert_to_decimal_number.py
# Lab_3d_sequences_bytearray.py
# Lab_3d_sequences_bytes.py
# Lab_3d_sequences_list.py
# Lab_3d_sequences_range.py
# Lab_3d_sequences_str.py
# Lab_3d_sequences_str_problem1.py
# Lab_3d_sequences_tuples.py
# Lab_3d_sets.py

# Print the name of the files start with Lab_1c
print("List of names start with Lab_1c")
for name in filenames:
    if name.startswith('Lab_1c'):
        print(name)
        
# List of names start with Lab_1c
# Lab_1c_add_two_int.py
