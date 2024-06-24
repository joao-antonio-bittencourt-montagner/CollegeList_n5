n = str(input('Digite um número romano: ')).upper()
l = []
c = c1 = 0
for i in range (len(n)):
    l.append(n[i])

while c1 < len(l):
    if l[c1] == 'I' and l[c1+1] == 'V':
        c += 4
        c1 += 2
        print('sim4')

    elif l[c1] == 'I' and l[c1+1] == 'X':
        c += 9
        c1 += 2
    
    elif l[c1] == 'I':
        c += 1
        c1 += 1
        print('sim1')
    elif l[c1] == 'V':
        c += 5
        c1 += 1
        print('sim5')
    elif l[c1] == 'X':
        c += 10
        c1 += 1

print(c)