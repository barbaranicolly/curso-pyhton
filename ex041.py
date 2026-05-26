total = 0
mil = 0
menor = 0
barato = ''
while True:
    print('----LOJA SUPER BARATAO----')
    produto = input('digite o nome do produto: ')
    preco = float(input('digite o preço do produto: '))
    continuar = input('quer continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('digite apenas S ou N: ').strip().upper()[0]
    if continuar == 'S':
        preco += total
        total += preco
    if preco > 1000:
         mil += 1
    if menor == 0 or preco < menor:
         menor = preco
         barato = produto
    elif continuar == 'N':
        break
print('----fim do programa----')
print(f'o total gasto na compra foi de {total}')
print(f' o produto mais barato foi o {barato}')
print(f'produtos acima e 1000: {mil}')