n = str('Quem parte reparte e fica com a maior parte').split()
n.pop()
n.append('parcela')
n1 = ''
for i in range(len(n)):
    n1 += n[i]
    n1 += ' '
print(n1)