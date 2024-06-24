from Funções import media
n1 = int(input('Quantas notas deseja colocar?'))
c = 0
for i in range(n1):
    c += int(input('Digite a sua nota aqui entre 1 a 10:'))
print(c)
c = c/n1
print(c)
print(media(c))