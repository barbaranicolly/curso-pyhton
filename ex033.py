
primeiro = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
 print(c)
