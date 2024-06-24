print('Vamos conferir se as palavras a seguir são palindromas.')
n = str(input('Digite uma palavra:'))
n1 = str(input('Digite outra palavra:'))
if n[::-1] == n1 or n1[::-1] == n:
    print('Essas palavras são palindromas')
else:
    print('Essas palavras não são palindromas')
