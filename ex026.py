salario = float(input('qual o valor do seu salario nensal RS: '))
salario_antigo = (salario * 10) / 100
novo_salario = salario + salario_antigo
novos = (salario * 15) / 100
novosa = salario + novos
if salario > 1250:
    print('seu novo salario com aumento de 10% é RS: {:.3f}'.format(novo_salario))
if salario < 1250:
    print('seu novo salario com aumento de 15% é RS: {:.3f}'.format(novosa))
