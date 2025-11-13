from random import randint
numeroDeRepeticoes = 0
win = 0
computador = randint(0, 10)
while win == 0:
    numeroDeRepeticoes += 1
    jogador = int(input('Tente adivinhar um número de 0 a 10: '))
    if jogador == computador:
        print(f'Parabéns você ganhou!\n'
              f'Número de tentativas: {numeroDeRepeticoes}')
        win = 1
    elif jogador > computador:
        print('Menos... Tente novamente!')
    else:
        print('Mais... Tente novamente!')
