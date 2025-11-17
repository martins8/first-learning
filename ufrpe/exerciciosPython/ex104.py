def leiaint(valor):
    while True:
        n = str(input(f'{valor}'))
        if n.isnumeric() is True and n.isdecimal() is True:
            return n
        else:
            print('\033[31mERROR! Informe um número inteiro positivo válido\033[m')


numero = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
