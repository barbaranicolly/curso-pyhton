s = n = 0
c = 1
while True:
    n = int(input('digite um valor: 999 faz parar: '))
    if n == 999:
        break
    s += n
c += 1
print(f'a soma dos {c} valores digitados, foi de {s}')