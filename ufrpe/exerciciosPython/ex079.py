lista = list()
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não será adicionado.')
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] ')).strip()
    if resposta in 'Nn':
        break
lista.sort()
print(lista)



