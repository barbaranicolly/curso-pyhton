from random import randint
vitorias = 0
print('----'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('----'*10)
while True:
    jogador = int(input('diga um valor: '))
    palpite = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    computador = randint(0, 10)
    total = jogador + computador
    print('----'*10)
    if total % 2 == 0:
        resultado = 'P'
        print(f'total de {total} e deu par')
    else:
        resultado = 'I'
        print(f'total de {total} e deu impar')
        if palpite == resultado:
                print('voce venceu')
                vitorias += 1
        else:
            print('voce perdeu')
        break
    print(f'game over! voce venceu {vitorias} vezes')

