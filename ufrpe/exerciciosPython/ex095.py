analiseJogador = dict()
listaGols = []
listaGols2 = []
listaGeral = []
while True:
    totalGols = 0
    analiseJogador['Nome do jogador'] = str(input('Nome do jogador: ')).strip()
    analiseJogador['Quantidade de partidas'] = int(input('Quantidade de partidas: '))
    for contador in range(1, analiseJogador['Quantidade de partidas']+1):
        listaGols.append(int(input(f'Quantidade de gols na partida {contador}: ')))
    analiseJogador['Quantidade de gols'] = listaGols[:]
    listaGols2.append(listaGols[:])
    for gols in listaGols:
        totalGols += gols
    analiseJogador['Total de gols'] = totalGols
    listaGeral.append(analiseJogador.copy())
    analiseJogador.clear()
    listaGols.clear()
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'{"_"*40}\n'
      f'{"cod  nome":<15} {"gols":<15} total\n'
      f'{"_"*40}')
for dados in listaGeral:
    print(f'{listaGeral.index(dados)}    {dados["Nome do jogador"]:9}{dados["Quantidade de gols"]}'
          f'{dados["Total de gols"]:>12}')
print(f'{"_"*40}')
while True:
    dadosJogador = int(input('Mostrar dados de qual jogador? (999 para terminar)'))
    if dadosJogador == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    elif dadosJogador > len(listaGeral):
        print(f'ERRO! Não existe jogador com código {dadosJogador}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {listaGeral[dadosJogador]["Nome do jogador"]}')
        for partida, gols in enumerate(listaGols2[dadosJogador]):
            print(f'No jogo {partida+1} fez {gols} gols.')
        print("_"*40)







