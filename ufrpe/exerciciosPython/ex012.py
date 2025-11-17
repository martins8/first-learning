preco = float(input('Informe o preço do produto: R$ '))
novopreco = preco - (preco*5/100)
print(f'Levando em conta o desconto de 5% no produto que vale R${preco}')
print(f'Seu novo preço será: R${novopreco:.2f}')



