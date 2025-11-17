tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
if tupla.count(9) == 0:
    print(f'O número 9 apareceu nenhuma vez')
else:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) == 0:
    print(f'O número três não está na tupla')
else:
    print(f'O número 3 está na posição {tupla.index(3)+1}')
print('Os valores pares digitados foram:', end=' ')
for valor in tupla:
    if valor % 2 == 0:
        print(f'{valor}', end=' ')








