lista = []
for indices in range(1, 6):
    lista.append(int(input(f'Digite o {indices}º número inteiro: ')))
print(f'O maior valor foi: {max(lista)} na(s) posição(ões):', end=' ')
for posicao, numero in enumerate(lista):
    if numero == max(lista):
        print(posicao, end=' ')
print('')
print(f'O menor valor foi: {min(lista)} na(s) posição(ões):', end=' ')
for posicao, numero in enumerate(lista):
    if numero == min(lista):
        print(posicao, end=' ')



