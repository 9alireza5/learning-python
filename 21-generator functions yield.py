print('difference between classic function and yield function ')
# classic function:
def firstn(n):
    nums = []
    for i in range(1,n+1):
        nums.append(i)
    return nums

for n in firstn(3):
    print(n,end=' ') # this is not a good approach
print('\n') #this means like an enter, goes to next line
# generator function:
def firstx(x):
    for i in range(1,x+1):
        yield i
for num in firstx(3):
    print(num,end=' ') #this is a good one
print('\n')
def firstnum (n):
    num=0
    while num<n:
        yield num
        num+=1
for num in firstnum(10):
    print(num, end=' ')