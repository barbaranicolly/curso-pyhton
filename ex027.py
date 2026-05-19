from random import randint
palpite= int(input('pedra: 1, papel: 2, 3:tesoura? '))
opcao = ["pedra, papel, tesoura"]
escolhapc= random.randint(0, 2)
if palpite == escolhapc:
    print('voce me venceu')
else:
    print('eu venci pois escolhi {}'.format(escolhapc))