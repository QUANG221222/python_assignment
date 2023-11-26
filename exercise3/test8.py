import random
computer=random.randint(1,50)
while(True):
    player=int(input("Enter your number choose:"))
    if(player==computer): 
        print(f"Your chose is right, the number random is:{computer}")
        break
    elif(player>computer): print("Your number is too high")
    else: print("Your number is too slow")
