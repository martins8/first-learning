# Capta duas notas e tira a média delas, dependendo do valor da média, informa qual a situação do estudante.
nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média é: {media:.1f}')
if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')

