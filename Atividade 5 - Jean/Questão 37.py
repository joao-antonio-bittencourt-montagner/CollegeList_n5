n = str(input('Dê um número binário:'))
r = 0
n = n[::-1]
for i in range(len(n)):
    if n[i] == '1':
        r += 2**i
print(r)