casa = float(input('qual o valor da casa? '))
salario = float(input('qual o salario mensal? '))
duracao = int(input('em quantos anos deseja pagar? '))
prestacao = casa / (duracao * 12)
limite =  salario * 30 / 100
if prestacao <= limite:
  print(' o valor da prestaçao sera de RS {:.2f} e pagara en {} anos'.format(prestacao, duracao))
else:
  print('a prestaçao da casa ficaria em {:.2f}, esta acima do seu rendimento mensal, o seu credito nao foi aprovado'.format(prestacao))