import math
n=int(input("Nhập số nguyên N: "))
if (n==2 or n==3): 
    print(f"{n} là số nguyên tố")
elif n%2==0:
    print(f"{n} ko phải là số nguyên tố")
elif n==1:
    print(f"{n} ko phải là số nguyên tố")

else: 
    i=2
    m=math.sqrt(n)
    while i<=m:
        i+=1
        if i%n!=0:
            print(f"{n} là số nguyên tố")
        else: print(f"{n} ko phải là số nguyên tố")
