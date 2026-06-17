prin = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(prin) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    prin.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N]: ')).upper()
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]: ')).upper()
    if resp in 'Nn':
        break

print(f'foram cadastradas {len(prin)} pessoas')
print(f'o maior peso foi de {maior}kg, peso de ', end='')
for p in prin:
    if p[1] == maior:
     print(f'[{p[0]}] ', end='')
print()
print(f'o menor peso foi de {menor}kg, foi de ', end='')
for p in prin:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')