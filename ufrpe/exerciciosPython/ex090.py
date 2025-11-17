dadosEscolares = {'Nome': str(input('Nome: '))}
dadosEscolares['Média'] = float(input(f'Média de {dadosEscolares["Nome"]}: '))
if dadosEscolares['Média'] >= 7:
    dadosEscolares['Situação'] = 'Aprovado'
else:
    dadosEscolares['Situação'] = 'Reprovado'
for keys, values in dadosEscolares.items():
    print(f'{keys} é igual a {values}')


