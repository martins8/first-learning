lista = []
for indices in range(1, 6):
    numeros = int(input('Digite um valor: '))
    if indices == 1 or numeros > lista[-1]:
        lista.append(numeros)
        print('Valor adicionado no final da lista...')
    else:
        for posicao, numero in enumerate(lista):
            if numeros <= lista[posicao]:
                lista.insert(posicao, numeros)
                print(f'Valor adicionado na posição {posicao} da lista')
                break
print(lista)
