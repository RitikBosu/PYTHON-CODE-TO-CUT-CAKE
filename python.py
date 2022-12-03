print("---------Welcome To The Python Programming----------")
print("My Name Is Ritik Bosu \nRes. No. 12211290")
print("Follow The Instruction Given Below") 
print("we have to find is it possible to cut cake in following cases")



cakeangle=int(input("Enter the Angle of the Cake: "))
N=int(input("Enter N: "))
if(cakeangle%N==0):
    print("YES the cake will cut in equal pieces of size %d"%N)
else:
    print("NO the cake will not cut in equal pieces of size %d"%N)
if(N>cakeangle):
    print("NO the cake will not cut in any piece of size %d"%N)
else:
    print("YES the cake will cut in any piece of size %d"%N)
if(cakeangle>0):
    print("Yes the cake will cut into %d pieces such that no two of them are equal"%N)
else:
    print("NO the cake will not cut into %d pieces such that no two of them are equal"%N)



print("Thank You, Bye Bye")
