numerosExtenso = ('zero', 'um', ' dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze'
                  , 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um número de 0 a 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente.')
    print(f'Você digitou o número {numerosExtenso[numero]}\n')
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S/N] ')).strip()
        if resposta in 'Nn':
            print('Obrigado pela utilização!')
    break
print('Finalizando...')
