# Break Statement
# The break statement can be used inside a for loop or while loop to come out of the loop.

# in For Loop
# for with else
# for( var in sequence ):
#    statements
# else:
#    statements
    
#searching for an element in a list
print("Searching element using for..break")
group1 = [1,2,3,4,5] #take a list of elements
search = int(input('Enter element to search:'))
for ele in group1:
    if search == ele:
        print('Element found in group1')
        break     #come out of for loop
else:
    print('Element not found in group1') #this is else suite

# in While loop
# while( condition ):
#    statements
# else:
#    statements

print("Searching element using while..break")
#Using break to come out of while loop
x = 10
while x>=1:
    print ('x=', x)
    x-=1
    if x==5: #if x is 5 then come out from while loop
        break
print("Out of loop")

