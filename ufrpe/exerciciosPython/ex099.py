from time import sleep


def maior(* valores):
    print(f'{"_"*40}\n'
          f'Analisando os valores passados...')
    for numeros in valores:
        print(numeros, end=' ')
        sleep(0.5)
    print(f' Foram informados {len(valores)} valores ao todo.\n'
          f'O maior valor foi: {max(valores)}')


maior(1, 3, 5, 7, 4, 1, 0)
maior(3, 5, 6, 9)
