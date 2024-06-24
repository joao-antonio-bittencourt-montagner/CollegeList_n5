from Funções import fatora1

n = int(input('Dê o valor da quantidade de alunos: '))
n1 = int(input('Dê o número de alunos de um grupo: '))
r = n - n1
r = n/(n1 * (n - n1))
print('A quantidade de possibilidades é: ',r)