resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
         if n > maior:
            maior = n
         if n < menor:
             menor = n
    resp= (input('quer continuar? S/N: ')). upper().strip()[0]
media = soma / quant
print(f'voce digitou {quant} numeros, e a media foi de {media}')
print(f'o maior valor foi {maior} e o menor {menor}')

