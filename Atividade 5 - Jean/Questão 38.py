def euclides():

    n1 = float(input('Digite o valor de x1: '))
    n2 = float(input('Digite o valor de x2: '))
    r1 = n1 - n2

    n3 = float(input('Digite o valor de y1: '))
    n4 = float(input('Digite o valor de y2: '))
    r2 = n3 - n4

    n5 = float(input('Digite o valor de z1: '))
    n6 = float(input('Digite o valor de z2: '))
    r3 = n3 - n4

    r = ((r1)**2 + (r2)**2 + (r3)**2)**0.5
    print('O valor da distância X e Y é:',r)

r = 0
euclides()



