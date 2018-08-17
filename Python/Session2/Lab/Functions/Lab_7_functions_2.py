# functions - Retun values
# return c 
# return 100
# return list1
# return a, b, c

# Case 1 - Returning single value
# define the add function
def add(a, b):
    return(a + b)                # returning single value

# call function int arguments
result1 = add(10, 20)
print(result1)

# call function float args
result2 = add(10.3, 40.3)
print("%.3f" %result2)



# Case 2 - Returning multiple values
# Syntax: return a, b, c
def arthematic_functions(a, b):

    x = a + b
    y = a - b
    z = a * b
    return x, y, z

print("store return values in e, f, g")
print("Values passed 10, 20")
e, f, g = arthematic_functions(10, 20)
print("+, -, *", e, f, g)

# Case 3 - Returning multiple values and store as tuple
# Syntax: return a, b, c
print("store return values in tuple tuple1")
print("Values passed 100, 50")
tuple1 = arthematic_functions(100,50)
print(type(tuple1))
print(tuple1)



