dados = dict()
listaDados = []
somatoriaIdade = mediaIdade = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = ' '
    while dados['Sexo'] not in 'MmFf':
        dados['Sexo'] = str(input('Sexo: [M/F] ')).strip()
    dados['Idade'] = int(input('Idade: '))
    somatoriaIdade += dados['Idade']
    listaDados.append(dados.copy())
    dados.clear()
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S/N]')).strip()
    if resposta in 'Nn':
        break
mediaIdade = somatoriaIdade / len(listaDados)
print(f'{"_"*40}\n'
      f'O grupo tem {len(listaDados)} pessoa(s)\n'
      f'A média de idade é de {mediaIdade} anos\n'
      f'As mulheres cadastradas foram: ', end='')
for dados in listaDados:
    if dados['Sexo'] in 'Ff':
        print(f'[{dados["Nome"]}]', end=' ')
print('\nLista das pessoas que estão acima da média: \n')
for dados in listaDados:
    if dados['Idade'] > mediaIdade:
        print(f'Nome: {dados["Nome"]}; Sexo: {dados["Sexo"]}; Idade: {dados["Idade"]}')




