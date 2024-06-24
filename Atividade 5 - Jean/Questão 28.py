from Funções import soma, sub, div, mult

def menu1(x):    
    print('-'*20)
    print('MENU')
    print('-'*20)
    print('[1]Soma\n[2]Subtração\n[3]Divisão\n[4]Multiplicação\n[5]Limpar memória\n[6]Sair')
    print('Estado da memória:', EM)
    print('-'*20)
    n = int(input('Escolha uma função:'))
    x = False
    if n == 1:
        soma(n)
    elif n == 2:
        sub(n)
    elif n == 3:
        div(n)
    elif n == 4:
        mult(n)
    elif n == 5:
        EM = 0
    elif n == 6:
        return(x)

x = True
x1 = False
while x1 != menu1(x):
    menu1(x)
    
    