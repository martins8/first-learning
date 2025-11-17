coletaDados = []
listA = []


def dados(nome, idade):
    coletaDados.append(nome)
    coletaDados.append(idade)
    listA.append(coletaDados[:])
    coletaDados.clear()


def showregistereds():
    print(f'{"-"*40}\n'
          f'{"PESSOAS CADASTRADAS":^40}\n'
          f'{"-"*40}')
    for posicao, dadoS in enumerate(listA):
        print(f'{dadoS[0]:<30} \t{dadoS[1]:>3}')

