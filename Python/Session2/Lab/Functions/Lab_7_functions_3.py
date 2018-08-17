# functions
# Notes:
# ------
# 1. In Python, functions are considered as first class objects.
# 2. It means we can use functions as perfect objects.
# 3. In fact when we create a function, the Python interpreter internally
#    creates an object.
# 4. Since functions are objects,
#       a. As we can pass a function to another function
#           just like we pass an object (or value) to a function.
#       b. Also, it is possible to return a function from another function.
#           This is similar to returning an object (or value) from a function.
# 5. To summarise, the following possibilities are noteworthy:
#        It is possible to define one function inside another function.
#        It is possible to pass a function as parameter to another function.
#        It is possible that a function can return another function.

print("Case1 - Define a function inside another function")
def display(str1):
    def display_more_message():
        return " More message"
    result = str1 + display_more_message()
    return result

# Call function and display
print(display("display"))

print("Case2 - Pass function as parameter to another function")
def display(fun):
    return 'Hai '+ fun

def message():
    return 'How are U? '
#call display() function and pass message() function
print(display(message()))

print("Case3 - Return function from another function")
#functions can return other functions
def display():
    def message():
        return 'How are U?'
    return message
#call display() function and it returns message() function
#in the following code, fun refers to the name: message.
fun = display()
print(fun())


