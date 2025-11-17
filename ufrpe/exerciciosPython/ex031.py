distancia = float(input('Qual a distância da viagem em km: '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f'O valor da sua passagem será: {passagem:.2f}')
