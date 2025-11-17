numero = int(input('Qual número você deseja ver a tabuada: '))
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f'{numero} * {multiplicador:2} = {resultado}')
