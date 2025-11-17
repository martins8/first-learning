def areaRetangulo(comp, larg):
    a = comp * larg
    print(f'A área desse terreno retângular com as dimensões {comp}x{larg} é: {a}m²')


comprimento = float(input('Informe o comprimento do terreno retângular: '))
largura = float(input('Informe a largura do terreno retângular: '))
areaRetangulo(comprimento, largura)

