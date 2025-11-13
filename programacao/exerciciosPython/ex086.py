lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linhas in range(0, len(lista)):
    for colunas in range(0, 3):
        lista[linhas][colunas] = int(input(f'Digite um valor para [{linhas}, {colunas}]: '))
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[ {lista[linhas][colunas]:^5} ]', end=' ')
    print()






