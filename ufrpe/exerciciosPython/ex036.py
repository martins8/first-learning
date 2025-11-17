# informa o valor da casa do salário e da quantidade de anos que o usuário desejará pagar o empréstimo
# se o valor da parcelar excerder 30% do salário informado, infelizmente, o usuário não poderá efetuar o empréstimo
valorCasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
nmrAnos = int(input('Em quantos anos desejará pagar o empréstimo? '))
valorParcelas = valorCasa / (nmrAnos * 12)
print(f'O valor da parcela será: R${valorParcelas:.2f}')
if valorParcelas > (salario * 30 / 100):
    print('Infelizmente, você não pode financiar está casa.')
else:
    print('Você está apto ao financiameno.')

