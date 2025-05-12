def is_prime(n):
    if n < 2:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True

my_dict = dict()
for i in range(10):
    key = int(input())
    counter = 0
    for j in range(2, key):
        if key % j == 0 and is_prime(j):
            counter += 1
    my_dict[key] = counter
max_count = max(my_dict.values())
candidates = [k for k, v in my_dict.items() if v == max_count]
best_number = max(candidates)

print(best_number, max_count)
