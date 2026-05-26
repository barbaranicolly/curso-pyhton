from random import randint
vitorias = 0
print('----'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('----'*10)
while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    print(f'game over! voce jogou {jogador} e o computador jogou {computador}. total de {total} ')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce venceu')
            vitorias += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu')
            vitorias += 1
        else:
            print('voce perdeu')
            vitorias += 1
            break
    print('vamos jogar novamente')
print(f'game over, voce venceu {vitorias} vezes')