a=input("Enter list number:  ")

if len(a)>0:
    list_number=[int(number) for number in a.split()]
    Max=max(list_number)
    Min=min(list_number)
    print("Max is:  ",Max, '\n', "Min is:  ",Min)
else: print("Nhập sai!!")
