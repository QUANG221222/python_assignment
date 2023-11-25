import random
random_num=[random.random() for _ in range(5)]

Maximum=max(random_num)
Minimum=min(random_num)

Average_num= sum(random_num)/len(random_num)


print("Random 5 number between 0 and 1: ", random_num)
print("Average of num: ",Average_num)
print("Max:  ",Maximum)
print("Min:  ",Minimum)