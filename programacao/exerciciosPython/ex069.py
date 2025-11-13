qntdMaioresDe18 = qntdHomens = mulheresComMenosD20a = 0
while True:
    print('=' * 25)
    print('CADASTRE UMA PESSOA')
    print('=' * 25)
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()
    while True:
        if sexo not in 'MmFf':
            sexo = str(input('Sexo: [M/F] ')).strip()
        else:
            break
    print('='*25)
    if idade > 18:
        qntdMaioresDe18 += 1
    if sexo in 'Mm':
        qntdHomens += 1
    if idade < 20 and sexo in 'Ff':
        mulheresComMenosD20a += 1
    resposta = str(input('Quer continuar? [S/N] ')).strip()
    while True:
        if resposta not in 'SsNn':
            resposta = str(input('Quer continuar? [S/N] ')).strip()
        else:
            break
    if resposta in 'Nn':
        break
print(f'A quantidade de pessoas cadastradas com mais de 18 anos foi: \033[31m{qntdMaioresDe18}\033[m\n'
      f'A quantidade de homens cadastrados foi: \033[32m{qntdHomens}\033[m homens\n'
      f'A quantidade de mulheres cadastradas com menos de 20 anos foi de: \033[33m{mulheresComMenosD20a}')











