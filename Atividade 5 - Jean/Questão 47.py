l = []
l1 = []
l2 = []
c = 1
r1 =  r2 = 0
for i in range(2):
    l1.append(int(input('Dê um valor para a matriz 2x2: ')))
    l2.append(int(input('Dê um valor para a matriz 2x2: ')))
l.append(l1)
l.append(l2)

for i in range(2):
    r1 += l[i][i]
    r2 += l[c][c]
    c -= 1
c = 2
for i in range(2):
    print(l[i], end='')
    if c == 2:
        print(r1)
        c -= 1 
    else:
        print(r2) 

