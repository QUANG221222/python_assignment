import random
num1=random.randint(0,9)
num2=random.randint(0,9)
if num1>num2:
    result=int(input(f"What is {num1} - {num2}?"))
    if result==num1-num2: print("You are correct!")
    else: 
        print("Your are is wrong.")
        print(f"{num1} - {num2} is",num1-num2)
else:
    result=int(input(f"What is {num2} - {num1}?"))
    if result==num2-num1: print("You are correct!")
    else: 
        print("Your are is wrong.")
        print(f"{num2} - {num1} is",num2-num1)
 