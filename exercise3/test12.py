width=int(input("Enter square's width:"))
height=int(input("Enter square's height:"))
for i in range(height):
    for j in range(width):
        print("*",end="")
    print()
print()
for i in range(height):
    for j in range(width):
        if i==0 or j==0 or i==height-1 or j==width-1:
            print("*",end=" ")
        else: print(" ",end=" ")
    print()
