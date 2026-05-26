total = totmil = menor = cont = 0
barato = ' '
while True:
    print('----LOJA SUPER BARATAO----')
    produto = input('digite o nome do produto: ')
    preco = float(input('digite o preço do produto : '))
    cont += 1
    total += preco
    if preco > 1000:
         totmil += 1
    if cont == 1 or preco < menor:
         menor = preco
         barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
            break
print('----fim do programa----')
print(f'o total gasto na compra foi de {total}')
print(f' o produto mais barato foi o {barato} que custa {menor}')
print(f'produtos acima e 1000: {totmil}')