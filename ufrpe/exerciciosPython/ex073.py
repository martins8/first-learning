campeonato = ('Brasil', 'Argentina', 'Equador', 'Uruguai', 'Peru', 'Chile', 'Colômbia', 'Bolívia', 'Paraguai',
              'Venezuela')
print(f'Ordem de classificação da eliminatória sul-americana para a copa do mundo:\n')
for contador in range(0, len(campeonato)):
    print(f' -{campeonato[contador]}', end='- ')
print()
print('-='*55)
print(f'Os cinco primeiros são: {campeonato[0:5]}')
print('-='*20)
print(f'Os quatro últimos são: {campeonato[-4:]}')
print('-='*20)
print(f'Seleções em ordem alfabética: {sorted(campeonato)}')





