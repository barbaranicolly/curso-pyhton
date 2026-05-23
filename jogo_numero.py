from random import randint
computador = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('digite o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais...')
        elif jogador > computador:
            print('menos...')
print(f'seu palpite foi o numero secreto, levou {palpite} chances para adivinhar')
