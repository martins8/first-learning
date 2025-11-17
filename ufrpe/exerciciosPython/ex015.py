dia = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de kms percorridos: '))
pagar = (60 * dia) + (0.15 * km)
print(f'Tendo em vista que o aluguel custa R$60 por dia\natrelado ao valor de R$0.15 por km rodado')
print(f'O valor final a ser pago será {pagar:.2f}')

