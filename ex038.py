s = cont = 0
while True:
    n = int(input('digite um valor (999 faz parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'a soma dos {cont} valores digitados, foi de {s}')