#trò chơi bao búa kéo
from random import randint
player= input()
computer= randint(0,2)

if computer== 0:
    computer="búa"
if computer== 1:
    computer="kéo"
if computer==2:
    computer="bao"


print("---")
print("Your choose:  " + player)
print("Computer chooses:  "+ computer)
print("---")

if player==computer:
    print("Dawn")
else:
    if player=="búa":
        if computer=="bao": 
            print("Lose")
        else:
            print("Win")

    elif player=="bao":
        if computer=="búa":
            print("Win")
        else:
            print("Lose")

    elif player=="kéo":
        if computer=="búa":
            print("Lose")
        else: 
            print("Win")
    else:
        print("Nhập sai rồi nhập lại đi!!!!!")
