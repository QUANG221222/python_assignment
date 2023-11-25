def UCNN(a,b):
    while a!=b:
        if a>b:
            a-=b
        else: b-=a
    return a

def BCNN(a,b):
    result=(a*b)/UCNN(a,b)
    return result

num1=int(input("Nhập số nguyên a: "))
num2=int(input("Nhập số nguyên b: "))
uoc=UCNN(num1,num2)
boi=BCNN(num1,num2)
print("Ước chung nhỏ nhất của a,b: ",round(uoc))
print("Bội chung nhỏ nhất của a,b: ",round(boi))