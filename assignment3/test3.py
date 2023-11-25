a=int(input("Nhập a: "))
b=int(input("Nhập b: "))

if a>b:
    print("a phải nhỏ hơn b mới tính được")
else:
    for num in range(a,b+1):
        if num%2 !=0:
            print(num)