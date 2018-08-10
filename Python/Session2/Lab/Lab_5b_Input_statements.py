# To input from user , python provides input() function.

# Case 1
print("*" * 10)
print("Case 1")
print("Usage of input()")
variable = input()
print(variable)
print("*" * 10)

# Case 2
print("Case 2")
print("Usage of input('some useful statements')")
variable = input("Enter Username: ")
print(variable)
print("*" * 10)

# Case 3
# since input returns string, if user enters variable it will also be in
# string. so we need to convert string to int? How ? using int() conversion
# method.
print("Case 3")
print("Usage of converting string numbers to int number")
num = input("Enter number")
print("Before conversion, type of variable")
print(type(num))
print("After converting to int, type of variable")
num1 = int(num)
print(type(num1))
print("*" * 10)

# short way num1 = int(input("Enter number"))
#           print(type(num1))

# Try for float also.

# Case 4
# Evaluating expression entered from keyboard
print("Case 4")
print("Evaluating expression entered from keyboard")

expr_val = eval(input("Enter the expression"))
print("Result = ", expr_val)
print("*" * 10)

# Case 5
# To accept list and display it
print("Case 5")
print("Accepting list from the input() method along with eval")
list1 = eval(input("Enter the list: "))
print(list1)
print("*" * 10)
# Try for tuple also.


