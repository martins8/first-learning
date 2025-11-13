from random import randint

# Algoritmo Insertion Sort
vetor = []
aux = 0

# trecho de código para preencher a lista apenas com números ímpares
for preencher in range(0, 30):
    numero = randint(0, 100)
    if numero % 2 == 0:
        while numero % 2 == 0:
            numero = randint(0, 100)
    vetor.append(numero)
    print(vetor)

    # a cada preenchimento, ocorrerá o algoritmo do Insertion Sort ordenando a lista corretamente
    for indice in range(0, len(vetor)):
        while indice > 0:
            if vetor[indice-1] > vetor[indice]:
                aux = vetor[indice]
                vetor[indice] = vetor[indice-1]
                vetor[indice-1] = aux
            indice -= 1


