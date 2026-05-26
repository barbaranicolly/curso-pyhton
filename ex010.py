while True:
    n = int(input('quer ver a tabuada de qual numero? '))
    if n < 0:
        print('programa encerrado. Volte sempre')
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('---' *20)