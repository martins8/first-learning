from datetime import date
anoAtual = date.today().year  # aposentadoria = 35 anos de colaboração
dados = dict()
dados['Nome'] = str(input('Nome: ')).strip()
dados['Idade'] = anoAtual - int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Ano de contratação'] + 35) - (anoAtual - dados['Idade'])
print('_'*40)
for keys, values in dados.items():
    print(f'{keys}: {values}')



