print('how if & else work')
age = 29
if age<30:
    situation = "ok"
    print(situation,'you are not that old')
else:
    situation = "hmmmmm"
    print(situation,'you are getting old')
print('-------------------------------')
print('how for & while work')
for i in range(1,6):
    print(i)
print('-------------------------------')
for j in range(1,7):
    if j%2==0:
        print(j,'is even')
    else:
        print(j,'is odd')
print('-------------------------------')
a = 0
while a < 5:
    print(a)
    a = a + 1