from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('digite o {} ano de nascimento: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
     totmenor += 1
print('{} ja sao maiores de idade e {} ainda nao sao maiores'.format(totmaior, totmenor))

