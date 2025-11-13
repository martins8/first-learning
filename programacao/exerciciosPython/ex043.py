# Lê do usuário o peso e a altura do mesmo. Calcula o IMC e diz em qual situação o usuário se encontra.
peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em m: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está com peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('CUIDADO! você se enquadra em um caso de OBESIDADE!')
else:
    print('CUIDADO! você se enquadra em um caso de OBESIDADE MÓRBIDA!')



