n = str(input('Digite uma seqência de números que representam um intervalo: '))
l= ['1','2','3','4','5','6','7','8','9']
n2 = []
for i in range(len(n)):
    for ii in range(len(l)):
        if n[i] == l[ii]:
            n2.append(l[ii])

for i in range(len(n2)):
    n2 = int(n2[i])