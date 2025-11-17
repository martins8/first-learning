# Lê o preço de um produto e a forma de pagamento que o usuário deseja efetuar para tal produto.
# De forma que adapte o preço em relação ao modelo escolhido pelo consumidor.
preco = float(input('Informe o preço do produto: R$ '))
print("""Informe a forma de pagamento: 
Digite [1] para efetuar o pagamento à vista (DINHERIO/CHEQUE) com 10% de desconto
Digite [2] para efetuar o pagamento à vista (CARTÃO) com 5% de desconto
Digite [3] para efetuar o pagamento em até 2x no cartão o preço continuará o padrão
Digite [4] para efetuar o pagamento em 3x ou mais vezes no cartão com 20% de juros""")
formaPagamento = int(input('Forma de pagamento a ser efetuada: '))
if formaPagamento == 1:
    novopreco = preco - (preco * 10 / 100)
    print(f"Você escolheu o pagamento à vista pelo dinheiro ou cheque e recebeu um desconto de 10%\n"
          f"O preço do produto antes R$ {preco}\nNovo preço com desconto R$ {novopreco:.2f}")
elif formaPagamento == 2:
    novopreco = preco - (preco * 5 / 100)
    print(f"Você escolheu o pagamento à vista pelo cartão e recebeu um desconto de 5%\n"
          f"O preço do produto antes R$ {preco}\nNovo preço com desconto R$ {novopreco:.2f}")
elif formaPagamento == 3:
    novopreco = preco / 2
    print(f"Você escolheu o pagamento no cartão em até 2x, o preço do produto não se modificará\n"
          f"Você deverá pagar duas vezes de R$ {novopreco:.2f}")
elif formaPagamento == 4:
    novopreco = preco + (preco * 20 / 100)
    parcelas = int(input('Informe a quantidade de parcelas em que desejará pagar: '))
    precoparcelado = novopreco / parcelas
    print(f"Você escolheu o pagamento no cartão em 3x ou mais vezes e, com isso, terá 20% de juros\n"
          f"O preço total a ser pago será R$ {novopreco}\n"
          f"Você deverá pagar {parcelas} vezes de R$ {precoparcelado:.2f}")
else:
    print("          ERROR\n"
          "Tente novamente informando uma opção válida")


