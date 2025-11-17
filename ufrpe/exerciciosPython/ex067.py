print('(Para encerrar o programa, digite um número negativo!)')
while True:
    numero = int(input('Qual número deseja ver a tabuada? '))
    if numero < 0:
        print('Processo FINALIZADO!')
        break
    print('-'*40)
    for multiplicador in range(1, 11):
        print(f'{numero} * {multiplicador:2} = {numero * multiplicador}')
    print('-'*40)



