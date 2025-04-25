from random import randint
print("for first round i'll guess compute's number")

a=randint(1,99)
answer=int(input())
while answer!=a:
    if answer>a:
        print('too high')
        answer = int(input())
    elif answer<a:
        print('too low')
        answer = int(input())
    if answer==a:
        print('you guessed right')
low=1
high=99
guess=randint(low,high)
print('')
print("now computers must guess my number")
print('my first guess is ',guess)
response=str(input())
while response!='d':
    if response=='k':
        high=guess-1
        guess=randint(low,high)
        print('my new guess is ',guess)
        response=str(input())
    if response=='b':
        low=guess+1
        guess=randint(low,high)
        print('my new guess is ',guess)
        response=str(input())
if response=='d':
    print("game is over. we both guessed each other's number ^_^")
