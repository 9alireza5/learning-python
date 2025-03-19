def even(i):
    if i % 2 == 0:
        return True
    else:
        return False
def odd(i):
    if i % 2 != 0:
        return True
    else:
        return False
first=1
second=2
upper_limit=int(input('please enter the upper limit of fibonacci series: '))
sum_even=0
sum_odd=0
while first<=upper_limit:
    if even(first):
        sum_even=sum_even+first
    if odd(first):
        sum_odd=sum_odd+first
    new=first+second
    first=second
    second=new
print('summation of even numbers is equal to ',sum_even,'and sum of odd numbers is ',sum_odd)
