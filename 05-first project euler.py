print('first euler project for numbers below 10')
a = 0
for i in range(1,10):
    if i % 3 == 0 or i % 5 == 0:
        a=a+i
print(a)
print('ok this shit works, now we go for numbers under 1000')
print('')
print('first euler project for numbers below 1000')
a = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        a=a+i
print(a)
print('')
print('trying to use a function')
def threesome(a):
    if a % 3 == 0 or a % 5 == 0:
        return True
    else:
        return False
sum=0 #if i put sum in line below 23, every time that i changes, sum return to zero. so i should put it outside the loop
for i in range(1,1000):
    if threesome(i):
        sum=sum+i
print(sum)
