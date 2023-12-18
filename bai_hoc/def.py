# import random
# def ndigit_random(n):
#     digit=random.randint(0,9)
#     while(digit!=0): digit=random.randint(0,9)
#     sum=digit
#     while(n>0):
#         digit=random.randint(0,9) 
#         print(digit)
#         sum+=digit*10**(n-1) 
#         n-=1
#     return sum
# n=int(input("Nhap n="))
# print(ndigit_random(n))  
def sum(num):
    sum=0
    for i in range(1,num+1):
       sum+=i/(i+1)
    return sum
def output(num):
    print("i","\t","m(i)")
    for i in range(1,num+1):
        print(i,"\t","{:.4f}".format(sum(i)))
output(20)
