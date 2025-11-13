# Lendo um número e informando qual é o maior
numero1 = int(input('Informe um número inteiro: '))
numero2 = int(input('Informe outro número inteiro: '))
if numero1 > numero2:
    print(f'O primeiro valor {numero1} é maior que o segundo {numero2}')
elif numero2 > numero1:
    print(f'O segundo valor {numero2} é maior que o primeiro {numero1}')
else:
    print('Os dois valores são iguais.')
