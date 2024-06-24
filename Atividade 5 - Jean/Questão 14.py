n1 = str(input('Digite o DDD do seu estado:'))
n = str(input('Digite o seu número de telefone:')).strip()
cont = ''
for i in range(len(n)):
    if n[i] == '-': 
        cont += '-'
    elif n[i] == ' ':
        cont += ' '

if cont == '-' or ' ' and len(n) == 8:
    n2 = n1
    n2 += ' 3'
    n2 += n

    print('O número de telefone é:', n2)

if len(n) == 7:
    n2 = n1
    n2 += ' 3'
    n2 += n

    print('O número de telefone é:', n2)