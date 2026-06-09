valores = []
while True:
    valores.append(int(input(('digite um valor: '))))
    resp = str(input('quer continuar [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'voce digitou {len(valores)} valores')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente: {valores}')
if 5 in valores:
    print('o numero 5 faz parte da lista')
else:
    print('nao foi digitado o numero 5')