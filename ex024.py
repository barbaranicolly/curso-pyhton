velocidade = float(input('qual a velocidade do carro? '))
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print('voce foi nultado em RS{:.2f}'.format(multa))
else:
   print('voce esta conduzindo na velocidade permitida')