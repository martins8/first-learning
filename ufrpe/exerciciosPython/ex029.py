v = float(input('Qual a velocidade do carro em km/h: '))
if v > 80:
    print('Você ultrapassou os limites de velocidade estabelecidos e será multado!')
    multa = (v - 80) * 7
    print(f'Sua multa custará: {multa}R$')
else:
    print('Tenha um bom dia e mantenha a direção segura!')



