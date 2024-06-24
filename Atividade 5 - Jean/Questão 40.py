n = int(input('Quantos números primos deseja ver? '))
r1 = r2 = r3 = r4 = c = 0
lp = []
ln = []
while True:
    c += 1
    r1 = c%2
    r2 = c%3
    r3 = c%5
    r4 = c%7 

    if c != 1 and c == 2 or c == 3 or c == 5 or c == 7:
        lp.append(c)
        if len(lp) == n:
            break

    elif c != 1 and r1 != 0 and r2 != 0 and r3 != 0 and r4 != 0:
        lp.append(c)
        if len(lp) == n:
            break
print(lp)