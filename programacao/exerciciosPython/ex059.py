resposta = 0
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('[1] PARA SOMAR OS VALORES\n'
      '[2] PARA MULTIPLICAR OS VALORES\n'
      '[3] PARA SABER QUAL É O MAIOR\n'
      '[4] PARA DIGITAR NOVOS NÚMEROS\n'
      '[5] PARA SAIR DO PROGRAMA')
while resposta != 5:
    resposta = int(input('Digite o número [ ]: '))
    if resposta == 1:
        soma = valor1 + valor2
        print(f'A soma dos valores {valor1} e {valor2} é: {soma}\n')
    elif resposta == 2:
        multiplicacao = valor1 * valor2
        print(f'A multiplicação dos valores {valor1} e {valor2} é: {multiplicacao}\n')
    elif resposta == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'O maior valor entre {valor1} e {valor2} é: {maior}\n')
    elif resposta == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        print('[1] PARA SOMAR OS VALORES\n'
              '[2] PARA MULTIPLICAR OS VALORES\n'
              '[3] PARA SABER QUAL É O MAIOR\n'
              '[4] PARA DIGITAR NOVOS NÚMEROS\n'
              '[5] PARA SAIR DO PROGRAMA')
    elif resposta == 5:
        print('Fim do programa!')
    else:
        print('ERROR\n'
              'INFORME UMA RESPOSTA VÁLIDA')




