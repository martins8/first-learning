resposta = ''
somatoria = maior = menor = qntdNumerosDigitados = 0
while resposta != 'N':
    numero = int(input('Digite um número inteiro: '))
    qntdNumerosDigitados += 1
    somatoria += numero
    if numero > maior:
        maior = numero
    if qntdNumerosDigitados == 1:
        menor = numero
    elif numero < menor:
        menor = numero
    resposta = str(input('Deseja continuar? [S ou N]: ')).strip().upper()
    if resposta != 'S' and resposta != 'N':
        print('ERROR\n'
              'Digite a resposta corretamente')
        quit()
media = somatoria / qntdNumerosDigitados
print(f'A média dos valores digitados foi: {media}\n'
      f'O maior valor foi: {maior}\n'
      f'O menor valor foi: {menor}')




