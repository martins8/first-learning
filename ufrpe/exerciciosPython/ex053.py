# verificador de frases/palavras palíndromas
frase = str(input('Diga uma frase ou palavra: ')).strip().upper()
palavras = frase.split()
frasejunta = ''.join(palavras)
print(f'Normal:  {frasejunta}')

fim = len(frasejunta) - 1
contrario = ''
for contador in range(fim, -1, -1):  # da para simplificar atribuindo o fatiamento [::-1] na variavel contrario
    contrario += frasejunta[contador]
print(f'Inverso: {contrario}')

if contrario == frasejunta:  # verificação se o contrário da frase é igual a ela normal.
    print(f'A frase/palavra é PALÍNDROMA')
else:
    print(f'A frase/palavra não é PALÍNDROMA')











