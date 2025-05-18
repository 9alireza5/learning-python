class Student:
    def __init__(self):
        self.class_a = []
        self.class_b = [] #if i don't use self.class, it only works inside this function, for working in all code i must use self.

    def input_data(self):
        a = int(input())
        ages = list(map(float, input().split()))
        heights = list(map(float, input().split()))
        weights = list(map(float, input().split()))
        for i in range(a):
            self.class_a.append((ages[i], heights[i], weights[i]))

        b = int(input())
        ages = list(map(float, input().split()))
        heights = list(map(float, input().split()))
        weights = list(map(float, input().split()))
        for i in range(b):
            self.class_b.append((ages[i], heights[i], weights[i]))

    def average_age(self, data):
        return sum(i[0] for i in data) / len(data)

    def average_height(self, data):
        return sum(i[1] for i in data) / len(data)

    def average_weight(self, data):
        return sum(i[2] for i in data) / len(data)

s = Student()
s.input_data()

a_age = s.average_age(s.class_a)
a_height = s.average_height(s.class_a)
a_weight = s.average_weight(s.class_a)

b_age = s.average_age(s.class_b)
b_height = s.average_height(s.class_b)
b_weight = s.average_weight(s.class_b)

print(a_age)
print(a_height)
print(a_weight)
print(b_age)
print(b_height)
print(b_weight)

if a_height > b_height:
    print("A")
elif b_height > a_height:
    print("B")
else:
    if a_weight < b_weight:
        print("A")
    elif b_weight < a_weight:
        print("B")
    else:
        print("Same")
