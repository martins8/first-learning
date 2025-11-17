firstTerm = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Digite a razão desejada para a PA: '))
qntdTermos = 10
contador = 1
otherTerms = firstTerm
print(firstTerm, end='')
resposta = 1
while resposta != 0:
    while contador != qntdTermos:
        otherTerms += razao
        print(f' → {otherTerms}', end='')
        contador += 1
    print('\n\nDeseja aumentar a quantia de termos calculados?\n'
          'Digite o número da quantia:\n'
          'Se não quiser digite 0')
    resposta = int(input('Sua opção: '))
    if resposta == 0:
        print(f'\nQuantidade de termos mostrados: {qntdTermos}\n'
              f'Obrigado pela utilização do programa, volte sempre!')
    else:
        qntdTermos += resposta




