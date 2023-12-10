#n=int(input("Nhập số nguyên n: "))
#first=0
#second=1
#i=2
#while i<=n:
 #   i+=1
 #   fib=first+second
 #   first=second
  #  second=fib
#print(f"{n} trong dãy fibonacci là {second}")
def fibonacci(num):
    if(num==0 or num==1): return num
    else: return fibonacci(num-1)+fibonacci(num-2)
n=int(input("Nhập số nguyên:"))
print(fibonacci(n))
