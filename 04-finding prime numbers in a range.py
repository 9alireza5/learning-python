print('In this code, I am using input for the first time and writing a code that identifies prime numbers within a specified range.')
def is_prime(p):
    if p < 2:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True
def prime(n):
    for i in range(2,n+1):
        if is_prime(i):
            print(i,'is prime')
        else:
            print(i,'is not prime')
a=int(input('please enter upper limit of the range: '))
prime(a)