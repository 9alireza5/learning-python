n = int(input())
participants = []

for i in range(n):
    parts = input().strip().split('.')
    gender = parts[0].lower()
    name = parts[1][0].upper() + parts[1][1:].lower()
    subject = parts[2]
    participants.append((gender, name, subject))

participants.sort(key=lambda x: (x[0], x[1]))

for p in participants:
    print(p[0], p[1], p[2])
