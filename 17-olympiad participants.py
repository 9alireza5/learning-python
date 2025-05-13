n = int(input())
participants = []
for i in range(n):
    participant = input().strip().lower().split('.')
    gender = participant[0]
    name = participant[1].capitalize()
    subject = participant[2]
    participants.append((gender, name, subject))

participants.sort(key=lambda x: (x[0], x[1]))

for p in participants:
    print(p[0], p[1], p[2])