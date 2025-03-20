print('in a room with 50 people and 100$ for each of them, with every snapp one random dude gives 1$ to a random person')
print('if someone,s money becomes 0, he will delete from the game')
import matplotlib.pyplot as plt
import random
random.seed()
people=[]
for i in range(0,50):
    people.append(100)
#print(people,'ok now we have 50 people with 100$ per person')
for snapp in range(0,10000):
    for person1 in range(0,50):
        person2=random.randrange(0,50)
        while people[person2]==0:
            person2=random.randrange(0,50)
        if people[person1]!=0:
            people[person1]=people[person1]-1
            people[person2]=people[person2]+1
print(people)
people.sort()
plt.bar(range(0,50),people)