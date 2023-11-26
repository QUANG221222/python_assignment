def prime(num):
    if(num<2): return False
    else:
        dem=0
        for i in range(1,num+1):
            if(num%i==0): dem+=1
        if(dem==2): return True
        else: return False
number=int(input("Enter number="))
if(prime(number)==True):
    print(f"{number} is Prime.")
else: print(f"{number} is not Prime.")
