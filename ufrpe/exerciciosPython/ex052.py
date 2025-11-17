numero = int(input('Informe um número para saber se ele é PRIMO ou não: '))
primo = 0
for contador in range(1, numero + 1):
    if numero % contador == 0:
        primo += 1
        print(f'\033[33m{contador}\033[m', end=' ')
    else:
        print(f'\033[31m{contador}\033[m', end=' ')
print('')
if primo <= 2:
    print(f'O número {numero} é primo\n'
          f'Pois ele possui apenas {primo} divisores')
else:
    print(f'O número {numero} NÃO é primo\n'
          f'Pois ele possui {primo} divisores')







