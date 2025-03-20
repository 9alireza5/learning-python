import matplotlib.pyplot as plt
import random
random.seed()
dice=[0,0,0,0,0,0]
#print('or we can use, for i in range (0,5) dice.append=0')
for turn in range(0,500000):
    number=random.randrange(0,6)
    dice[number]=dice[number]+1
print(dice)
plt.bar(range(1,7),dice)