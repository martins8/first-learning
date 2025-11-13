somaPares = 0
cont = 0
for contador in range(1, 7):
    numero = int(input(f'Informe o {contador}º número: '))
    if numero % 2 == 0:
        somaPares += numero
        cont += 1
print(f'Foram obtidos {cont} valores pares e a soma entre eles resulta em: {somaPares}')


