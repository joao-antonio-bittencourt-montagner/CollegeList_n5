n = str(input('Escreva uma frase: '))
n1 = str(input('Escreva outra frase: '))
c = ''
if len(n) > len(n1):
    c = n

else:
    c = n1

n2 = ''
for i in range(len(c)):
    if i < len(n): 
        n2 += n[i]

    if i < len(n1):
        n2+= n1[i]

print(n2)