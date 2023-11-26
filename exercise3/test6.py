import random
computer=random.randint(10,100)
chu_so_dau_computer=int(computer/10)
chu_so_cuoi_computer=int(computer%10)
player=int(input("Enter two-digit a number:"))
chu_so_dau_player=int(player/10)
chu_so_cuoi_player=int(player%10)
print("The random number is:",computer)
if computer==player: print("The award is $10,000")
elif (chu_so_dau_player==chu_so_cuoi_computer) and (chu_so_cuoi_player==chu_so_dau_computer): print("The award is $3,000")
elif (chu_so_dau_player==chu_so_dau_computer) or (chu_so_dau_player==chu_so_cuoi_computer) or (chu_so_cuoi_player==chu_so_dau_computer) or (chu_so_cuoi_player==chu_so_cuoi_computer):
    print("The award is $1,000")
else: print("Your guess is wrong")