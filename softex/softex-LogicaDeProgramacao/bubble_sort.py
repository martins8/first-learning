vetor = [3, 2, 1, 6, 4, 5]
print(vetor)
fim = len(vetor)
indice = 0

for indice in range(fim-1):
    for indice2 in range(fim-1):
        if vetor[indice] > vetor[indice+1]:
            aux = vetor[indice]
            vetor[indice] = vetor[indice + 1]
            vetor[indice+1] = aux
            print(vetor)
