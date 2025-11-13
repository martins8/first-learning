analiseJogador = dict()
listaGols = []
totalGols = 0
analiseJogador['Nome do jogador'] = str(input('Nome do jogador: ')).strip()
analiseJogador['Quantidade de partidas'] = int(input('Quantidade de partidas: '))
for contador in range(1, analiseJogador['Quantidade de partidas']+1):
    listaGols.append(int(input(f'Quantidade de gols na partida {contador}: ')))
analiseJogador['Quantidade de gols'] = listaGols[:]
print('_'*40)
for keys, values in analiseJogador.items():
    print(f'{keys}: {values}')
print('_'*40)
print(f'O jogador {analiseJogador["Nome do jogador"]} jogou {analiseJogador["Quantidade de partidas"]} partidas.')
for partidas, gols in enumerate(listaGols):
    print(f'      => Na partida {partidas+1} fez {gols} gols.')
    totalGols += gols
print(f'O total de gols foi de {totalGols}')




