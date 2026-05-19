from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''suas opcoes: 
[0] pedra
[1] papel
[2] tesoura''')
palpite= int(input('qual a sua jogada? '))
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[palpite]))
if   computador == 0:
    if palpite == 0:
      print('empate')
    elif palpite == 1:
      print('jogador vence')
    elif palpite == 2:
     print('computador vence')
    else:
      print('opcao invalida')
elif computador == 1:
      if palpite == 0:
         print('computador vence')
      elif palpite == 1:
           print('empate')
      elif palpite == 2:
          print('jogador vence')
      else:
         print('opcao invalida')
elif computador == 2:
     if palpite == 0:
         print('jogador vence')
     elif palpite == 1:
          print('computador vence')
     elif palpite == 2:
          print('empate')
     else:
         print('opcao invalida')