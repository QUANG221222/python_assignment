length=int(input("Enter size of triangle:"))
for i in range(length):
    for j in range(i+1):
      print("*",end=" ")
    print()
print("\t")
for i in range(length,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("\t")
for i in range(1, length + 1):
    khoang_trang = length - i
    print(" " * khoang_trang + "*" * i)
