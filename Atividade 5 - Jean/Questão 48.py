lista = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lista1 = []

n = str(input('Digite uma frase: ')).upper()
c = 0

for i in range(len(n)):
    lista1.append(n[i])

for i in range(len(lista)):
    if lista[i] in lista1:
        c += 1

if c == 26:
    print('Essa frase é um prangrama')
else:
    print('Essa frase não é um pangrama.')