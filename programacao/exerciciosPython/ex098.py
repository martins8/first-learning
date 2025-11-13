from time import sleep


def contador(i, f, p):
    if p == 0:
        p = -1
    if i > f and p > 0:
        p *= -1
    if i > f:
        print(f'Contagem de {i} até {f} de {p*-1} em {p*-1}')
        for numero in range(i, f-1, p):
            print(numero, end='  ')
            sleep(0.4)
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        for numero in range(i, f+1, p):
            print(numero, end='  ')
            sleep(0.4)
    print()
    print('_'*30)


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é suua vez de personalizar a contagem')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('_'*30)
contador(inicio, fim, passo)
