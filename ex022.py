num = int(input('digite um numero inteiro: '))
print('qual sera a base de conversão? ')
print('1 para binario')
print('2 para octal')
print('3 para hexadecimal')
opcao = int(input('digite sua opçao: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)))