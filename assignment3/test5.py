def add(x,y):
    return x+y

def Subtract(x,y):
    return x-y

def Multiply(x,y):
    return x*y

def Divide(x,y):
    if y==0:
        print("You can\'t divide 0")
    else: return x/y

print("----Operations----")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
print("------------------")

q="Y"
while q=="Y":
    c= int(input("Please choose operations (1,2,3,4):"))
    if c>=5:
        print("Your choose is invalid")
    else:
        num1=float(input("Enter number 1: "))
        num2=float(input("Enter number 2: "))
    if c==1:
        print("Result add: ",add(num1,num2))
    elif c==2:
        print("Result Subtract: ",Subtract(num1,num2))
    elif c==3:
        print("Result Multiply: ",Multiply(num1,num2))
    elif c==4:
        print("Result Divide: ",Divide(num1,num2))
    q=input("Do you want to continue (Y/N)?\n")