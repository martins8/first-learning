nmr = int(input('Informe um número de 0 a 9999: '))
un = nmr // 1 % 10
d = nmr // 10 % 10
c = nmr // 100 % 10
m = nmr // 1000 % 10
print(f'Unidade: {un}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')



