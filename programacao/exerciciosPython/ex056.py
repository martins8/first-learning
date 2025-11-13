somatoriaIdade = 0
homemMaisVelho = ''
idadeComparativa = 0
mulheresMenosDe20a = 0
for contador in range(1, 5):
    nome = str(input(f'Informe o {contador}º nome: ')).strip().upper()
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: [M / F] ')).strip().upper()
    somatoriaIdade += idade
    print('')
    if idade > idadeComparativa and sexo == 'M':
        idadeComparativa = idade
        homemMaisVelho = nome
    if idade < 20 and sexo == 'F':
        mulheresMenosDe20a += 1
mediaIdade = somatoriaIdade / 4
print(f'A média das idades obtidas é de \033[31m{mediaIdade}\033[m\n'
      f'O nome do homem mais velho com {idadeComparativa} anos é: \033[32m{homemMaisVelho}\033[m\n'
      f'A quantidade de mulhers com menos de 20 anos é de \033[33m{mulheresMenosDe20a}')














