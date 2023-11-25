list_of_number=input("Enter your list:  ")
Number=[int(number) for number in list_of_number.split(",")]
print(len(Number),"\n",sum(Number))