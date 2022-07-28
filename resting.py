import random

# seed random number generator
randomlist = []
for i in range(0, 49):
    n = random.randint(95, 100)
    randomlist.append(n)
print(randomlist)
