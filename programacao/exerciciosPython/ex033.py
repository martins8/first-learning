n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
else:
    if n2 < n3:
        menor = n2
    else:
        menor = n3
print(f'O maior número foi: {maior}')
print(f'O menor número foi: {menor}')

