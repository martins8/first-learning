sexo = str(input('Informe o seu sexo [M / F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Informe o seu sexo [M / F]: ')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')


