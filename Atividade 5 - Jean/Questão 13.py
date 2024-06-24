n = str(input('Digite uma frase:'))
lista = ['a', 'e', 'i', 'o', 'u', ' ']
lista1 = [0, 0, 0, 0, 0, 0]

for i in range(len(n)):
    if n[i] in lista:
        if n[i] == 'a':
            lista1[0] += 1
        
        elif n[i] == 'e':
            lista1[1] += 1

        elif n[i] == 'i':
            lista1[2] += 1
        
        elif n[i] == 'o':
            lista1[3] += 1
        
        elif n[i] == 'u':
            lista1[4] += 1

        elif n[i] == ' ':
            lista1[5] += 1

print(f'A frase possui {lista1[5]} espaços, {lista1[0]} letras A, {lista1[1]} letras E, {lista1[2]} letras I, {lista1[3]}', end='')
print(f' letras O e {lista1[4]} letras U')