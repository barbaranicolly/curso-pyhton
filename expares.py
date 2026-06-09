valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('digite um valor: ')))
    resp = str(input('quer continuar: [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'a lista completa é {valores}')
print(f'os numeros pares são {pares}')
print(f'os numeros impares são {impares}')