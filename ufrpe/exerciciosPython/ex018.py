from math import radians, cos, sin, tan
nmr = float(input('Informe um ângulo qualquer: '))
C = cos(radians(nmr))
S = sin(radians(nmr))
T = tan(radians(nmr))
print(f'O número {nmr}\nPossui o cosseno igual a: {C:.2f}\nPossui o seno igual a: {S:.2f}')
print(f'Por fim a tangente vale: {T:.2f}')

