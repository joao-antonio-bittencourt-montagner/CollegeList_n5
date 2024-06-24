n = str(input('Digite o seu  e-mail:'))
c = 0
c = n.find('@gmail.com')
print(c)
if c != 0 and c != -1:
    print('O seu e-mail é válido.')
else:
    print('E-mail inválido.')