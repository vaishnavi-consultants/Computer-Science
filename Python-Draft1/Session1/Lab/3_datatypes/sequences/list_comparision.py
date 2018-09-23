# List Comparision

print("List Comparision")

L = [1,2,3]
M = [1,2,3]

print("Using (L == M) operator")
if L == M:
    print("Same values")

print("Using (L is M) operator")
if L is M:
    print("Same")
else:
    print("id of L",id(L))
    print("id of M",id(M))
    print("L and M are different objects")
