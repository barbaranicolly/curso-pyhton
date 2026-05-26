mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    nome = str(input('digite o {}º nome: '.format(p))).strip()
    idade = int(input('digite a idade: '))
    sexo = str(input('digite o sexo: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
     maioridadehomem = idade
     nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
     maioridadehomem = idade
     nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('a media das idades é de {}'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))
