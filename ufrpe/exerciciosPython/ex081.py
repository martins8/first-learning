lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N]')).strip()
    if resposta in 'Nn':
        break
print(f'A quantidade de números digitados foi: {len(lista)}')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente: {lista}')
if lista.count(5) >= 1:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não faz parte da lista')
