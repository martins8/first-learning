salario = float(input('Informe o seu salário R$: '))
if salario > 1250:
    salarionovo = salario + (salario * 10 / 100)
    print(f'Tendo em vista que seu salário é: {salario}')
    print(f'Seu novo salário com aumento de 10% será: {salarionovo}')
else:
    salarionovo = salario + (salario * 15 / 100)
    print(f'Tendo em vista que seu salário é: {salario}')
    print(f'Seu novo salário com aumento de 15% será: {salarionovo}')


