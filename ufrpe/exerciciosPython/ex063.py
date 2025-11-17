numero = int(input('Digite o número de termos que deseja obter \n'
                   'nos primeiros valores da sequência de fibonacci\n'
                   'O número de termos sequênciais: '))
contador = 1
x = 0
y = 1
print(f'{x} → {y}', end='')
while contador != numero - 1:
    f = x + y
    print(f' → {f}', end='')
    x = y
    y = f
    contador += 1







