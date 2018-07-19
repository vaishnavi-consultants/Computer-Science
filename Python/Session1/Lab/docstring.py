# command
# python.exe -m pydoc -w docstring

# program with two functions
def add(x ,y):
    '''
    This function takes two numbers and finds their sum.
    it displayes the sum as result.
    '''
    print("Sum = ", (x+y))

def message():
    '''
    This function displays a message.
    This is a welcome message to the user.
    '''    
    print("Welcome to python")


# now call the functions
add(10,25)
message()

# Results
# Sum =  35
# Welcome to python
# wrote docstring.html
