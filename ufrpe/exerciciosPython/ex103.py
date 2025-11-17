def ficha(nome='', gols=''):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if gols.isnumeric() and gols.isdecimal() is True:
        gols = int(gols)
    else:
        gols = '0'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nomeJogador = str(input('Nome do jogador: ')).strip()
golsJogador = str(input('Número de gols: ')).strip()
print(ficha(nomeJogador, golsJogador))

