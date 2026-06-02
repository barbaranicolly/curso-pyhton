valores = []
resp = ''
while True:
    n = int(input('digite um valor: '))
    if n in valores:
        print('valor duplicado, nao sera adicionado.')
    else:
        valores.append(n)
        print('valor adicionado com sucesso...')
    resp = str(input('quer continuar? [S/N]:')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
print('---'*10)
valores.sort()
print(f'voce digitou os valores: {valores} ' , end='')