qntdNumerosDigitados = somatoria = numero = 0
print('Somatoria de números\n'
      'Para finalizar digite 999')
while numero != 999:
    numero = int(input('Digite algum número inteiro: '))
    if numero != 999:
        qntdNumerosDigitados += 1
        somatoria += numero
    else:
        print('Obrigado pela utilização do programa, volte sempre!')
print(f'Total de número digitados: {qntdNumerosDigitados}\n'
      f'Somatoria dos números digitados: {somatoria}')






