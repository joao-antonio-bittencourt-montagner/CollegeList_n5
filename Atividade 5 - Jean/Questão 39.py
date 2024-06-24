import random

def met(a):
    if len(a) <= 1:
        return a
    
    meio = len(a)//2
    le = a[:meio]
    ld = a[meio:]

    pe = met(le)
    pd = met(ld)

    return mm(pe , pd)

def mm(e, d):
    l = []
    i = j = 0
    while i < len(e) and j <len (d):
        if e[i] < d[j]:
            l.append(e[i])
            i += 1
        else:
            l.append(d[j])
            j += 1

    l.extend(e[i:])
    l.extend(d[j:])

    return l

p = 16
l5 = [random.randint(1,99)for i in range(p)]
print(met(l5))