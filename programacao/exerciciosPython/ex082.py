lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S / N] '))
    if resposta in 'Nn':
        break
listaImpares = []
listaPares = []
for posicao, numeros in enumerate(lista):
    if numeros % 2 == 0:
        listaPares.append(lista[posicao])
    else:
        listaImpares.append(lista[posicao])
print(f'A lista completa é {lista}\n'
      f'A lista de pares é {listaPares}\n'
      f'A lista de ímpares é {listaImpares}')



