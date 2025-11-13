valor = float(input('Informe um valor em metros: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print(f'O valor obtido {valor:.2f}m\nConvertido para km é: {km:.2f}km\nConvertido para hm é: {hm:.2f}hm')
print(f'Convertido para dam é: {dm:.2f}dam\nConvertido para decímetros {dm:.2f}dm')
print(f'Convertido para centimetros é: {cm:.2f}cm\nConvertido para milimetros é: {mm:.2f}mm')



