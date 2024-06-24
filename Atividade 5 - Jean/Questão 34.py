import random

def organizador():
    l1 = l.copy()
    l2 = []
    menor = 99
    pos =  0
    
    for i in range(t):
        for j in range(len(l1)):
            if menor > l1[j]:
                menor = l1[j]
                pos = j

        l2.append(menor)
        l1.pop(pos)
        menor = 99

    return l2

t = 10
l = [random.randint(1,99) for i in range(t)]

print(organizador())