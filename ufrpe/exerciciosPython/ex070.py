print('='*35)
print('LOJA SUPER BARATÃO')
print('='*35)
total = produtosMaisD1000 = precoMaisBarato = 0
nomeMaisBarato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        produtosMaisD1000 += 1
    if precoMaisBarato == 0 or preco < precoMaisBarato:
        precoMaisBarato = preco
        nomeMaisBarato = produto
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] ')).strip()
    if resposta in 'Nn':
        break
print('FIM DO PROGRAMA\n'
      f'O total da compra foi R${total:.2f}\n'
      f'Teve {produtosMaisD1000} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {nomeMaisBarato} que custa R${precoMaisBarato:.2f}')










