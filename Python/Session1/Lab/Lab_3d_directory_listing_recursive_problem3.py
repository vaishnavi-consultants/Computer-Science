# List contents of directories (files and subdirectories) - 1st Level only.
import os

# Method 2
# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
#    print("root ", root)
#    print("dirs ", dirs)
#    print("files ", files)
    path = root.split(os.sep)
#   print(path)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)

# Result
# ------
# --- Builtin_datatypes.txt
# --- Lab_1c_add_two_int.py
# --- Lab_3b_docstring.html
# --- Lab_3b_docstring.py
# --- Lab_3c_Types.txt
# --- Lab_3c_variables.txt
# --- Lab_3d_bool_datatype.txt
# --- Lab_3d_converting_datatypes.txt
# --- Lab_3d_convert_to_other_numbersystem.py
# --- Lab_3d_dictionary.py
# --- Lab_3d_directory_listing_recursive_problem3.py
# --- Lab_3d_ii_convert_to_decimal_number.py
# --- Lab_3d_i_convert_to_decimal_number.py
# --- Lab_3d_sequences_bytearray.py
# --- Lab_3d_sequences_bytes.py
# --- Lab_3d_sequences_list.py
# --- Lab_3d_sequences_range.py
# --- Lab_3d_sequences_str.py
# --- Lab_3d_sequences_str_problem1.py
# --- Lab_3d_sequences_str_problem2.py
# --- Lab_3d_sequences_tuples.py
# --- Lab_3d_sets.py
# --- Python(Final_Lists_Dictionary_Lab).docx
# --- ReadMe.txt
# --- __pycache__
# ------ Lab_1c_add_two_int.cpython-36.pyc
# ------ Lab_3b_docstring.cpython-36.pyc

# Method: 1 ( Top and next level directory listing only )
# This will explains the concept of isdir, etc.
# filenames = os.listdir('.')
# print("List of file name")

# for name1 in filenames:
#    if os.path.isdir(name1):
#        print("Contents of : ", name1)
#        subdir_filenames = os.listdir(name1)
#        for name2 in subdir_filenames:
#            print(name2)
#    else:
#        print(name1)

