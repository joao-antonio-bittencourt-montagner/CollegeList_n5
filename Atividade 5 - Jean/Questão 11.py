n = str(input('Digite uma frase:'))
n1 = str(input('Digite outra frase:'))
print(f'O tamanho de "{n}" é:', len(n))
print(f'O tamanho de "{n1}"é:', len(n1))

if n1 == n:
    print('O conteúdo das frases é a mesma.')

if len(n1) == len(n):
    print('As duas strings possuem o mesmo tamanho.')