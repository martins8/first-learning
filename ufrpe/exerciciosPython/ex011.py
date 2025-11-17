largura = float(input('Informe a largura em metros da parede: '))
altura = float(input('Informe a altura em metros da parede: '))
area = largura * altura
tinta = area / 2
print(f'A parede com largura equivalente a: {largura:.2f}m\nCom a altura valendo: {altura:.2f}m')
print(f'Possui a área valendo: {area:.2f}m²\nPara pintá-la, será necessário {tinta}l de tinta')
