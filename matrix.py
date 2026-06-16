prin = []
temp = []
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    prin.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N]: '))
    if resp in 'Nn':
            break

print(prin)