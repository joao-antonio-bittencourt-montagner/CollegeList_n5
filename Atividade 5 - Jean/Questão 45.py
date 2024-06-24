import random
n = int(input('Quantas colunas essa matriz possui? '))
n1 = int(input('Quantas linhas essa matriz possui? '))
n2 = [[random.randint(1,5)for i in range(n)]for i in range(n1)]
confL = []
list = []
conf = r = 0
r = n * n1
for i in range(n1):
    print(n2[i])


for i in  range(n1):
    conf = 0
    for ii in range(n):
        conf += n2[i][ii]
    
    confL.append(conf)

print('')
print(confL)
list.append(confL)
confL.clear()

for i in range(n):
    conf = 0
    for ii in range(n1):
        if i == ii:
            conf += n2[i][ii]
    confL.append(conf)

print('')
print(confL)
list.append(confL)
confL.clear()

for i in  range(n1):
    conf = 0
    for ii in range(n):
        conf += n2[ii][i]
    
    confL.append(conf)

print('')
print(confL)
list.append(confL)
confL.clear()

conf = 0
for i in  range(n):
    for ii in range(n1): 
        if n2[0][0] == n2[i][ii]:
            conf += 1

if conf == r:
    print('A matriz é um quadrado mágico')