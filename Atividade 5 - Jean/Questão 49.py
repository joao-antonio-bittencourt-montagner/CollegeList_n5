n = str(input('Digite uma sequência de números que representam um intervalo por -: '))
l= []
e = d = c = 0
for i in range(len(n)):
    print(i)
    if n[i] == '-':
        e = n[i-1]   
        d = n[i+1]
        e = int(e)
        d = int(d)
        print(e)
        print(d)
        while e < d:
             l.append(e)
             e += 1
        l.append(d)
        
    if n[i] not in l and n[i] != '-' and n[i] != ',':
        l.append(n[i])
l2 = []
for i in range(len(l)):
    c = l[i]
    c = int(c)
    if c not in l2:
        l2.append(c)
# 1-3,5,6,7-9
print(n)
print(l)
print(l2)


# 1,5,6-8,9
