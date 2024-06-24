n = str(input('Digite qualquer coisa:'))
c = 0
n1 = []
n2 = []
f = []
f1 = ''
for i in range(len(n)):
    if n[i] not in n1: 
        n1.append(n[i])
n1.sort()

for i in range (len(n1)):
    n2.append(n1[i])
    f.append(n1[i])

    for ii in range(len(n)):
        if n[ii] == n2[i]:
            c += 1

    n2.append(c)
    f.append(c)
    c = 0

print(n)            
print(sorted(n1))
print(f)
