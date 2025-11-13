def ajuda(escolhido):
    from time import sleep
    mensagem = f'ACESSANDO O MANUAL DO COMANDO "{escolhido}"'
    tamanhomsg = len(mensagem) + 4
    print(f'\033[42m{"~"*tamanhomsg}\n'
          f'\033[42m  {mensagem}  \n'
          f'\033[42m{"~"*tamanhomsg}')
    sleep(1.3)
    print('\033[m', end='')
    print('\033[7m')
    help(escolhido)
    print('\033[m')


print(f'\033[46m{"-" * 60}\033[m\n'
      f'\033[46m{"SISTEMA DE AJUDA PYTHON":^60}\033[m\n'
      f'\033[46m{"-" * 60}\033[m')
while True:
    funcaoOuBiblioteca = str(input('Informe a função ou biblioteca: ')).strip()
    if funcaoOuBiblioteca != 'FIM':
        ajuda(funcaoOuBiblioteca)
    else:
        break
