n = int(input("please enter a number "))

for i in range(0,n):

    for k in range (0, n-i):
        print(" ", end=" ")
    

    for j in range(0,i+1):
        print('#', end=" ")

    
    for m in range(0,1):
        print("  ",end="")
  
    for l in range(0, i+1):
        print("#", end=" ")
    
    print()



