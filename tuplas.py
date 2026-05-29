cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
num = ''
while num not in range(0, 21):
    num = int(input('digite um numero entre 0 e 20: '))
print(f'voce digitou o numero {cont[num]}')

