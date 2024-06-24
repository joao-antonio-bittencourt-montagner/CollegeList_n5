import random

def ordem(a):
    l2 = []
    for i in range(len(a)):
        if a[i] not in l2:
            l2.append(a[i]) 
    
    return l2

d = 10
l  = [random.randint(0,20)for i in range(d)]
print(l)
print('')
print(ordem(l))
