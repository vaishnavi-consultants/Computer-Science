# Using pass to do nothing
# The pass statement does not do anything. It is used with ‘if’ statement or inside
# a loop to represent no operation. We use pass statement when we need a
# statement syntactically but we do not want to do any operation.

x = 0
while x<10:
    x+=1
    if x>5: #if x > 5 then continue next iteration
        pass
    print ('x=', x)
print("Out of loop")

 
