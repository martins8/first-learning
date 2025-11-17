print('O programa irá rodar até a hora que você desejar\n'
      'Caso quiser parar o programa digite 999')
qntdnumerosDigitados = somatoria = 0
while True:
    numeros = int(input('Digite um número inteiro: '))
    if numeros == 999:
        break
    qntdnumerosDigitados += 1
    somatoria += numeros
print(f'A quantidade de números digitados foi: {qntdnumerosDigitados}\n'
      f'A somatoria dos números resultou em: {somatoria}')

