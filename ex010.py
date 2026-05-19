c = 0
soma = 0
n = soma + c
while n != 999:
      n = int(input('digite um numero: '))
      if n != 999:
         c += 1
         soma += n
print(f'foram digitados {c} numeros e a soma deles é {soma}')