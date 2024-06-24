n = str(input('Insira uma string: '))
l = [0, 0, 0]

for i in range(len(n)):
    if n[i] == '(':
        l[0] -= 1
    elif n[i] == '[':
        l[1] -= 1
    elif n[i] == '{':
        l[2] -= 1
    elif n[i] == ')':
        l[0] += 1
    elif n[i] == '[':
        l[2] += 1
    elif n[i] == '{':
        l[2] += 1
        
if all(i == 0 for i in l):
    print('Os parênteses estão alinahados.')

else:
    print('Os parenteses não estão alinhados.')