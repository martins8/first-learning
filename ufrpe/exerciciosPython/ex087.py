matriz = [[], [], []]
somaPares = somaTerceiraColuna = 0
for linhas in range(0, 3):
    for colunas in range(0, 3):  # aqui adiciona os elementos na lista, sendo considerado como coluna
        matriz[linhas].append(int(input(f'Digite um valor para [{linhas}, {colunas}]:  ')))
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
        if coluna == 2:
            somaTerceiraColuna += matriz[linha][2]
        print(f'[ {matriz[linha][coluna]} ]', end=' ')
    print()
print(f'A soma dos valores pares é {somaPares}\n'
      f'A soma dos valores da terceira coluna é {somaTerceiraColuna}\n'
      f'O maior valor da segunda linha é {max(matriz[1])}')
