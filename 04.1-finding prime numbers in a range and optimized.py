print('In this code, I am using input for the first time and writing a code that identifies prime numbers within a specified range.')
def is_prime(p):
    if p < 2:
        return False
    for i in range(2, int(p**0.5) + 1):  # Check divisibility up to sqrt(p)
        if p % i == 0:
            return False
    return True
def prime(n):
    print("Prime numbers in the range are:")
    for i in range(2, n + 1):
        if is_prime(i):
            print(i, end=" ")
a = int(input('Please enter the upper limit of the range: '))
prime(a)