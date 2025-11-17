print('='*40)
print('{:^40}'.format('BANCO CEV'))
print('='*40)
pedido = int(input('Que valor você quer sacar? R$'))
cedulasSacadas = [0, 0, 0, 0]
saque = pedido
while saque != 0:
    if saque >= 50:
        saque -= 50
        cedulasSacadas[0] += 1
    elif 50 > saque >= 20:
        saque -= 20
        cedulasSacadas[1] += 1
    elif 20 > saque >= 10:
        saque -= 10
        cedulasSacadas[2] += 1
    else:
        saque -= 1
        cedulasSacadas[3] += 1
print(f'Total de {cedulasSacadas[0]} cédulas de R$50\n'
      f'Total de {cedulasSacadas[1]} cédulas de R$20\n'
      f'Total de {cedulasSacadas[2]} cédulas de R$10\n'
      f'Total de {cedulasSacadas[3]} cédulas de R$1')













