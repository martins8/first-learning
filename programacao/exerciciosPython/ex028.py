from random import randint
n = randint(0, 5)
print('     NÚMERO DA SORTE\n  ')
n1 = int(input('Informe um número de 0 a 5: '))
if n1 == n:
    print('PARABÉNS, você acertou o número!')
else:
    print(f'Número escolhido pelo computador {n}')
    print(f'Número escolhido por você foi {n1}')
    print('Infelizmente, você não conseguiu, tente novamente!')


    


