""" numero = int(input('Digite o número que deseja obter o FATORIAL: '))
fatorial = numero
for contador in range(1, numero):
    fatorial = fatorial * contador
print(fatorial) """

numero = int(input('Digite o número que deseja obter o FATORIAL: '))
fatorial = numero
contador = 1
while contador < numero:
    fatorial = fatorial * contador
    contador += 1
print(f'{numero}! = {fatorial}')











