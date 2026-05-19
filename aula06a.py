sexo = str(input('digite o sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmmFf':
    sexo = str(input('dados invalidos, por favor informe seu sexo: ')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso')