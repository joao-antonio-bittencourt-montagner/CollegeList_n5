n = str(input('Digite uma sentença:')).lower().split()
n2 = ''
while True:
    n1 = str(input('Deseja sesurar alguma palavra? Se sim, qual? Se não, digite [N]')).lower()

    if n1 == 'n':
        break

    for i in range(len(n)):
        if n[i] == n1:
            n[i] = '*' * len(n[i])
    
    for i in range(len(n)):
        n2 += n[i]
        n2 += ' '

    print(n2)
    n2 = ''


