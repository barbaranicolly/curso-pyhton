num = (int(input('digite um numero: ')),
       int(input('digite outro numero: ')),
       int(input('digite mais um numero: ')),
       int(input('digite o ultimo numero: ')))
print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('o valor 3 nao foi digitado em nenhuma posição')
print('os valores pares digitados foram ', end='')
for n in num:
    if n% 2 == 0:
        print(n, end='')