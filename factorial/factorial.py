def factorial_with_loop(n):
   # factorial=1
   # for i in range(1, n+1):
   #     factorial*=i
   # return factorial
   if(n==0): return 1
   else: return n*factorial_with_loop(n-1)
number=int(input("Enter number:  "))
result=factorial_with_loop(number)
print(f"Factorial {number} is {result}")