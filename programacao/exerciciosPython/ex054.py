from datetime import date
anoAtual = date.today().year
qntdMenorDe18 = 0
qntdMaiorDe18 = 0
for contador in range(1, 8):
    anoNascimento = int(input(f'Informe o ano de nascimento da {contador}ª pessoa: '))
    if anoAtual - anoNascimento >= 21:
        qntdMaiorDe18 += 1
    else:
        qntdMenorDe18 += 1
print(f'A quantidade de pessoas que já atingiram a maioridade foi: {qntdMaiorDe18}\n'
      f'A quantidade de pessoas que ainda não antingiram a maioridade foi: {qntdMenorDe18}')






