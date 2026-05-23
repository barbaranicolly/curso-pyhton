while True:
    n = int(input('quer ver a tabuada de qual numero? '))
    if n < 0:
        print('programa encerrado. Volte sempre')
        break
    c = 1
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
    print('---' *20)