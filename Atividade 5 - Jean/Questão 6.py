print('Vamos verificar se duas palavras são um anagrama.')
n = str(input('Digite uma palavra:'))
n1 = str(input('Digete outra palavra:'))
c = 0
for i in range(len(n)):
    if n[i] in n1 and n1[i] in n and len(n) == len(n1):
        c += 1

if c == len(n):
    print('Essa palavra é um anagrama.')
    
else:
    print('Essa palavra não é um anagrama')