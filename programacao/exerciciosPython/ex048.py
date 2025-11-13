somaImpares = 0
contagem = 0
for numero in range(1, 501):
    if numero % 2 == 1 and numero % 3 == 0:
        somaImpares += numero
        contagem += 1
print(f'A soma dos ímpares múltiplos de três, os quais totalizam {contagem} números, é: {somaImpares}')

