import math
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))

if a==0:
    if b==0:
        if c==0:
            print("Phương trình vố số nghiệm")
        else: print("Phương trình vô nghiệm")
    else:print("Phương trình bậc 1:",-c/a)
else:
    d=b**2-4*a*c
    if d<0: print("Phương trình vô nghiệm")
    elif d==0: print("Phương trình nghiệm kép",-b/2*a)
    elif d>0:
        print("Phương trình có 2 nghiệm: ")
        print("x1=",(-b+math.sqrt(d))/2)
        print("x1=",(-b-math.sqrt(d))/2)

    