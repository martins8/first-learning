from random import randint
from time import sleep


def sorteio(lst):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lst.append(randint(0, 10))
        print(f'{lst[c]}', end=' ')
        sleep(0.3)
    print()


def somapares(lst):
    s = 0
    for numeros in lst:
        if numeros % 2 == 0:
            s += numeros
    print(f'A soma dos pares de {lst} '
          f'resulta em: {s}')


lista = []
sorteio(lista)
somapares(lista)
