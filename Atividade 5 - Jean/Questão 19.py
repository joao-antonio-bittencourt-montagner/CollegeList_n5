n = str(input('Digite qualquer frase:')).split()
n2 = n[::-1]
n3 =''
n1 = ''
for i in range(len(n)):
    n1 += n2[i]
    n1 += ' '
    n3 += n[i]
    n3 += ' '
print('')
print(n3)
print(n1)