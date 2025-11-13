from math import sqrt
CA = float(input('Informe o cateto ADJACENTE: '))
CO = float(input('Informe o cateto OPOSTO: '))
H = sqrt((CA**2) + (CO**2))
print(f'Com o cateto ADJACENTE valendo: {CA}\n Com o cateto OPOSTO valendo: {CO}')
print(f'A hipotenusa será igual a: {H:.2f}')

