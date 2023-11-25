import random
choices=['bao','bua','keo']
c=[random.random() for _ in range(5)]
print(random.randint(1,9))
print(random.choice(choices))
print(c)
print(random.uniform(1.0,5.0))
print(random.randrange(90,1000))
print(random.randbytes(8))
random.seed(100)

