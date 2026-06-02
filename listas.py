valores = []
for cont in range(0, 5):
   valores.append(int(input(f'digite um valor para a posiçao {cont}: ')))
print(f'voce digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'o maior valor digitado foi {maior} nas posiçoes: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i)
print(f'o menor valor digitado foi {menor} nas posiçoes: ', end ='')
for i, v in enumerate(valores):
    if v == menor:
        print(i, end='')