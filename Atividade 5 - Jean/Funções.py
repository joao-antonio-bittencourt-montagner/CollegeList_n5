def mes(m):

    n = ""
    if m == 1:
        n = "Janeiro"
    elif m == 2:
        n = "Fevereiro"
    elif m == 3:
        n = "Marco"
    elif m == 4:
        n = "Abril"
    elif m == 5:
        n = "Maio"
    elif m == 6:
        n = "Junho"
    elif m == 7:
        n = "Julho"
    elif m == 8:
        n = "Agosto"
    elif m == 9:
        n = "Setembro"
    elif m == 10:
        n = "Outubro"
    elif m == 11:
        n = "Novembro"
    elif m == 12:
        n = "Dezembro"
    else:
        print("Digite um mes valido")
    return(n)

def corretor(txt):
    c = str(txt).lower().replace('á', 'a').replace('ó','o').replace('í', 'i').replace('é','e').replace('ú','u').replace('ç','c')
    return(c)

def media(m):
    c = ''
    if m < 4:
        c = 'Reprovado'

    elif m == 4 or m < 7:
        c = 'Retorno suplementar'

    else:
        c = 'Aprovado'

    return(c)

def bist(b):
    r = ''
    c = b
    c1 = b
    c2 = b
    c = c%4
    c1 = c1%100
    c2 = c2%400

    if c == 0 and c2 != 0:
        r = 'True - Ano bissexto'

    elif c2 == 0 and c2 == 0:
        r = 'True -Ano bissexto'

    else:
        r = 'False - O ano possui 365 dias.'

    return(r)

def forma(v):
    import math
    pi = math.pi
    r = 0
    c = 0
    if v == 1:
        r = float(input('Dê o raio do círculo:'))
        c = 2*pi*r
        r = pi*r**2
        print('O valor do perímetro da figura é:', c)
        print('O valor da área da área é:', r)
        
    elif v == 2:
        b = float(input('Dê o valor da base do triângulo:'))
        h = float(input('Dê o valor da altura desse triângulo:'))
        l1 = float(input('Dê o valor de um lado desse triângulo:'))
        l2 = float(input('Dê o valor do outro lado desse triângulo:'))
        c = b*h/2
        r = h + l1 + l2
        print('O valor da área da figura é:', c)
        print('O valor do perímetro da figura é:', r)

    elif v == 3:
        b = float(input('Dê o valor da base do retângulo'))
        h = float(input('Dê o valor da altura do retângulo'))
        z = b*h
        p = 2*(b+h)
        print('O valor da área da figura é de:', z)
        print('O valor do perímetro da figura é de', p)

def soma(n):
    n = 0
    while True:
        n += float(input('Dê um valor para ser adicionado:'))
        print('O valor da soma é:', n)
        s = str(input('Deseja continuar somando? [S/N]')).lower()
        if s == 'n':
            break

def sub(n):
    n = 0
    n = float(input('Dê um valor para ser subtraído:'))
    n -= float(input('Dê outro valor a ser subtraído:'))
    print('O resultado é:', n)

def div(n):
    n = z = 0
    n = float(input('Dê um valor para ser dividido:'))
    z = float(input('Dê outro valor a ser o divisor:'))
    n = n/z
    print('O resultado é:', n)

def mult(n):
    n = z = 0
    n = float(input('Dê um valor para ser multiplicado:'))
    z = float(input('Dê outro valor a ser multiplicado:'))
    n = n * z
    print('O resultado é:', n)

def sominha(x):
    n3 = 0
    n = float(input('Dê o valor 1: '))
    n1 = float(input('Dê o valor 2: '))
    n3 = n + n1
    print('O valor da soma é:', n3)

def fatora(n):
    n = int(input('Dê um número:'))
    n1 = []
    r = 1
    for i in range(n):
        n1.append(n)
        n -= 1

    for i  in range(len(n1)):
        r = n1[i] * r

    return r
    
def fibonacci(n):
    n = int(input('Dê quantos números da sequência fibonacci você deseja.'))
    z = 0
    z1 = 1
    z2 = 0
    for i in range(n):
        
        z = z1 + z2
        z1 = z2
        z2 = z
        
        print(z)

def primo(n):
    n = int(input('Digite um número:'))
    r = r1 = r2 = r3 = r4 = 0
    # 2,3,5,7,9
    r1 = n%2
    r2 = n%3
    r3 = n%5
    r4 = n%7

    if n == 2 or n == 3 or n == 5 or n == 7:
        print('O seu número é primo.')

    elif n == 1 or n == 0 or n < 0 or r != 0:
        print('O seu número não é primo.')    

    elif r1 == 0 or r2 == 0 or r3 == 0 or r4 == 0:
        print('O seu número é normal')

    else:
        print('O seu número é primo')

def medi(n):
    n = int(input('Quantos números deseja adicionar à lista?'))
    n1 = []
    r = 0
    for i in range(n):
        n1.append(int(input('Digite um valor:')))

    for i in range(n):
        r += n1[i]

    r = r/n

    print(r)

def abv(n):

    abv = {'vc':'você',
           'cmg':'comigo',
           'lgc':'lógico',
           'q':'que'}
    
    t = n.split()
    tx = []

    for i in t:
        if i.lower() in abv:
            tx.append(abv[i.lower()])
        else:
            tx.append(i.lower())

    return' '.join(tx)

def dic(n):
    dados = {}
    for i in n:
        if i in dados:
            dados[i] += 1
        else:
            dados[i] = 1

    for p, i in dados.items():
        if i > 1:
            print(f'A palavra {p} aparece {i} vezes')
        else:
            print(f'A palavra {p} aparece {i} vez')

def fatora1(n):
    n1 = []
    r = 1
    for i in range(n):
        n1.append(n)
        n -= 1

    for i  in range(len(n1)):
        r = n1[i] * r
        
    return r

def voga(n):
    n.lower()
    c = 0
    list = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(n)):
        if n[i] in list:
            c += 1

    return c