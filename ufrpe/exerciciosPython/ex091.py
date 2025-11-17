from random import randint
from time import sleep
playersandPlay = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6),
                  'jgoador4': randint(1, 6)}
print('Valores sorteados: ')
for keys, values in playersandPlay.items():
    print(f'   O {keys} tirou {values}')
    sleep(0.5)
print(f'Ranking dos jogadores: ')
c = 1
for i in sorted(playersandPlay, key=playersandPlay.get, reverse=True):
    print(f'   {c}º lugar: {i} com {playersandPlay[i]}')
    c += 1













