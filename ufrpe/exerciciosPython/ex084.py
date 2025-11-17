coletaDados = list()
listaDados = list()
maiorPeso = menorPeso = 0
while True:
    coletaDados.append(str(input('Nome: ')))
    coletaDados.append(float(input('Massa: ')))
    listaDados.append(coletaDados[:])
    if coletaDados[1] > maiorPeso:
        maiorPeso = coletaDados[1]
    if menorPeso == 0:
        menorPeso = coletaDados[1]
    elif coletaDados[1] < menorPeso:
        menorPeso = coletaDados[1]
    coletaDados.clear()
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar [S/N] '))
    if resposta in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(listaDados)} pessoas\n'
      f'O maior peso foi de {maiorPeso:.2f}Kg. Peso de ', end='')
for verify in range(0, len(listaDados)):
    if listaDados[verify][1] == maiorPeso:
        print(f'[{listaDados[verify][0]}]', end=' ')
print(f'\n'
      f'O menor valor foi de {menorPeso:.2f}Kg. Peso de ', end='')
for verify in range(0, len(listaDados)):
    if listaDados[verify][1] == menorPeso:
        print(f'[{listaDados[verify][0]}]', end=' ')




