import ex115listagem


def cadastro():
    print(f'{"-"*40}\n'
          f'{"NOVO CADASTRO":^40}\n'
          f'{"-"*40}')
    name = str(input('Nome: '))
    idade = int(input('Idade: '))
    return ex115listagem.dados(name, idade)

