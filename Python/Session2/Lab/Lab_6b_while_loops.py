# while statement
# to print 1 to 10

max_no = 10
i = 0

# with single condition
print("Printing numbers 0 to 9[Single condition]")
while i < max_no:
    print(i, end=',')
    i+=1

print('\n')

# with multiple conditions
# print numbers between 10 to 20
print("Printing numbers 10 to 20 [multiple condition]")
i = 10
while i>=10 and i<=20:
    print(i,end=',')
    i+=1;
