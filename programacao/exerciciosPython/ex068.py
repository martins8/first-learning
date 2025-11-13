from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR!')
print('=-'*15)
vitoriasConsecutivas = 0
while True:
    maquina = randint(0, 10)
    jogador = int(input('Diga um valor de 0 até 10: '))
    if jogador > 10 or jogador < 0:
        print('Digite um valor válido')
        break
    jParOuImpar = str(input('Par ou Ímpar [P / I] ')).strip().upper()
    somatoria = jogador + maquina
    if somatoria % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    if jParOuImpar == 'P' and somatoria % 2 == 0 or jParOuImpar == 'I' and somatoria % 2 == 1:
        print(f'Você ganhou parabéns!\n'
              f'Sua jogada: {jogador}\n'
              f'Computador: {maquina}\n'
              f'Totalizando: {somatoria}\n'
              f'Resultando: {resultado}')
        vitoriasConsecutivas += 1
        print('=-'*15)
    else:
        print(f'Infelizmente, você perdeu.\n'
              f'Sua jogada: {jogador}\n'
              f'Computador: {maquina}\n'
              f'Totalizando: {somatoria}\n'
              f'Resultando: {resultado}')
        print('=-'*15)
        break
print(f'Vitorias Consecutivas: {vitoriasConsecutivas}')








