valores = list()
valor = list()
pares = list()
impares = list()
for c in range(1, 5):
    valor.append(int(input(f'digite o {c}º valor: ')))
    valores.append(valor[:])
    valor.clear()
    if c % 2 == 0:
        pares.append(valor[:])
    else:
        impares.append(valor[:])
valores.sort()
print(f'valores em ordem crescente: {valores}')
print(f'os pares sao {pares}')
print(f'os impares sao {impares}')