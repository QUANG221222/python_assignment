num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
while(num1!=num2):
   if(num1>num2): num1-=num2
   else: num2-=num1
print(num1)

