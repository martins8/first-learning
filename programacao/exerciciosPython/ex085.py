lista = [[], []]
for contador in range(1, 8):
    numero = int(input(f'Digite o {contador}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}\n'
      f'Os valores ímpares digitador foram: {lista[1]}')




