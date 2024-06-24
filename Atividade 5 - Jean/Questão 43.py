import random

d = 10

l = [random.randint(1,20)for i in range(d)]
l1 = [random.randint(1,20)for i in range(d)]
l3 = []

print(l)
print(l1)

for i in range(len(l1)):
    if l[i] in l1 and l[i] not in l3:
        l3.append(l[i])

print(l3)