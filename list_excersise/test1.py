#Create function reverse string
""" def reverse(string):
    return string[::-1]
string=input("Enter string: ")
result=reverse(string)
print(result) """
#Find longest length of word in list and display word
""" def longestLength(list,n):
    max=len(list[0])
    char=list[0]
    for i in range(1,n):
        if max<len(list[i]):
            max=len(list[i])
            char=list[i]
    print(max)
    print(char)
num=int(input("Enter size of list: "))
list=[]
for i in range(num):
    valid=input(f"list[{i}]")
    list.append(valid)
longestLength(list,num) """
#
""" def A(list,num):
    for i in range(num):
        list.append(float(input(f"List[{i}]=")))

num=int(input("Enter size of list: "))
list=[]
A(list,num)
list.reverse()
print(list)
element=input("Enter element: ")
list.insert(num,element)
print(list) """
""" l2=[3.0,4.0,5.0,3.0]
x=float(input("Enter x to find position: "))
for i in range(len(l2)):
    if l2[i]==x:
        print("All position of x in list is :",i) """
numbers = [1, 5, 2, 5, 9, 5, 2]
i=0
x=2
while(i<len(numbers)):
    if numbers[i]==x:
        numbers.remove(numbers[i])
    i+=1
print(numbers)

