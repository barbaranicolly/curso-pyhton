opcao = 0
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
print('-----------------')
print('-------menu------')
print('[1] somar')
print('[2] multiplicar')
print('[3] maior')
print('[4] novos numeros')
print('[5] sair do programa')
print('-----------------')
while opcao != 5:
    opcao = int(input('digite sua opcao: '))
    if opcao == 1:
        print(n1 + n2)
    elif opcao == 2:
        print(n1 * n2)
    elif opcao == 3:
        if n1 > n2:
            print(n1)
        elif n1 < n2:
            print(n2)
    elif opcao == 4:
       n1 = int(input('digite um novo numero: '))
       n2 = int(input('digite outro numero: '))
    if opcao == 5:
        print('fim do programa')