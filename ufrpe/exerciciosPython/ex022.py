nome = str(input('Informe o seu nome: ')).strip()
print(f'Nome em maísculas: {nome.upper()}')
print(f'Nome em minusculas: {nome.lower()}')
nome1 = nome.split()
nome2 = len(nome) - nome.count(' ')
nome3 = len(nome1[0])
print(f'Tem {nome2} letras sem contar os espaços')
print(f'Seu primeiro nome tem: {nome3} letras')







