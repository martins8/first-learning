# Jokenpô, a pessoa dirá qual jogada decidirá fazer: PEDRA, PAPEL ou TESOURA e, por fim, saberá se ganhou ou
# não comparando com a jogada da máquina
from random import choice
from time import sleep
print('---JOKENPÔ---')
opcaoMaquina = ['PEDRA', 'PAPEL', 'TESOURA']
jogadaPlayer = str(input('Escolha se você vai querer jogar entre\n'
                         'PEDRA, PAPEL OU TESOURA: ')).strip().upper()
jogadaMaquina = choice(opcaoMaquina)
print('JO...')
sleep(0.5)
print('KEN...')
sleep(1)
print('PO!!!')
if jogadaPlayer == 'PEDRA' and jogadaMaquina == 'TESOURA' or jogadaPlayer == 'TESOURA' and jogadaMaquina == 'PAPEL' \
        or jogadaPlayer == 'PAPEL' and jogadaMaquina == 'PEDRA':
    print(f'Jogada do computador: {jogadaMaquina}\n'
          f'Você ganhou, PARABÉNS!!!')
elif jogadaPlayer == 'PEDRA' and jogadaMaquina == 'PAPEL' or jogadaPlayer == 'TESOURA' and jogadaMaquina == 'PEDRA' \
        or jogadaPlayer == 'PAPEL' and jogadaMaquina == 'TESOURA':
    print(f'Jogada do computador: {jogadaMaquina}\n'
          f'Infelizmente, você perdeu.')
elif jogadaPlayer == jogadaMaquina:
    print(f'Jogada do computador: {jogadaMaquina}\n'
          f'O jogo deu empate!')
else:
    print('ERROR')










