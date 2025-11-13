# algoritmo que converte o número inteiro informado, para algumas das opções de conversões disponibilizadas.
numeroInt = int(input('Informe um número inteiro qualquer: '))
print('Escolha uma das maneiras de conversões disponibilizadas:\n'
      '[ 1 ] Converter para BINÁRIO\n'
      '[ 2 ] Converter para OCTAL\n'
      '[ 3 ] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'O número {numeroInt} convertido em BINÁRIO será: {bin(numeroInt)[2:]}')
elif opcao == 2:
    print(f'O número {numeroInt} convertido em OCTAL será: {oct(numeroInt)[2:]}')
elif opcao == 3:
    print(f'O número {numeroInt} convertido em HEXADECIMAL será: {hex(numeroInt)[2:]}')
else:
    print('--ERROR--\n'
          'Informe alguma opção válida')
