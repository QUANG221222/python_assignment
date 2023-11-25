import random
def random_number(n):
    if n<=1:
        return "Nhập phải lớn hơn 1"
    else:
        tren=10**(n-1)
        duoi=10**n-1
        ran=random.randint(tren,duoi)
        return ran
result=random_number(5)
print(result)
