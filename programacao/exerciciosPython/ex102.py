def fatorial(numero, show=False):
    """
        -> Calcula o Fatorial de um número
        :param numero: o número a ser calculado o seu fatorial.
        :param show: (opcional) mostrar ou não a conta.
        :return: O valor do Fatorial do 'numero' escolhido.
    """
    f = 1
    if show is True:
        for c in range(numero, 0, -1):
            f *= c
            if c > 1:
                print(f'{c} *', end=' ')
            else:
                print(f'{c} = ', end='')
        return f
    else:
        for c in range(numero, 0, -1):
            f *= c
        return f


print(fatorial(5, show=True))
