import random
d = 3
dd = d - 1
l = [[random.randint(1,1) for i in range(d)]for i in range (d)]
rs = j = jj = 0
lr = []
lr1 = {}

for i in range(d):
    print(l[i])
    

for i in range(d):
    for ii in range(d):
        rs += l[i][ii]
    
    lr.append(rs)
    rs = 0
lr1['Linhas'] = lr[:]
lr.clear()


for i in range(d):
    for ii in range(d):
        rs += l[ii][i]
    
    lr.append(rs)
    rs = 0
lr1['Colunas'] = lr[:]
lr.clear()


for i in range(d):
    for ii in range(d):
        if i == ii:
            rs += l[i][ii]
    
lr.append(rs)
rs = 0
lr1['Diagonal-D'] = lr[:]
lr.clear()


for i in range(d):
    for ii in range(d):
        if i == ii:
            rs += l[i][dd]
            print(dd)
            dd -= 1
            
lr.append(rs)
rs = 0
lr1['Diagonal-E'] = lr[:]
lr.clear()
print(lr1)

c = 0
if lr1['Linhas'] == lr1['Colunas']:
    if lr1['Diagonal-D'] == lr1['Diagonal-E']:
        for e in lr1['Linhas']:
            if e in lr1['Diagonal-D']:
                c += 1
            if c == d:
                print('Cocoricó')
