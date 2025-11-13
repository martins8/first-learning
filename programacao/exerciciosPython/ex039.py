# Informa através da idade de uma pessoa, se já pode se alistar, se ainda precisa esperar ou caso já esteja atrasado
# informa em ambos os casos o ano em que deve ser alistado ou os anos de atraso.
from datetime import date
anoAtual = date.today().year
print(f'O ano atual é {anoAtual}')
genero = str(input('Qual seu sexo? MASCULINO ou FEMININO? ')).strip().upper()
if genero == 'MASCULINO':
    anoNascimento = int(input('Informe o ano do seu nascimento: '))
    if anoAtual - anoNascimento < 18:
        anoAlistamento = 18 - (anoAtual - anoNascimento)
        print(f'Você ainda não pode se alistar, seu alistamento está previsto para daqui a {anoAlistamento} anos')
    elif anoAtual - anoNascimento == 18:
        print('Você está na idade correta para se alistar.')
    else:
        anoAlistamento = (anoAtual - anoNascimento) - 18
        print(f'Você está atrasado com o seu alistamento faz {anoAlistamento} anos, agende o mais rápido possível')
elif genero == 'FEMININO':
    print('Você não precisa fazer alistamento militar obrigatório.')
else:
    print('Informação inválida.')

