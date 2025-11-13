# Através da idade, informa a categoria do atleta.
from datetime import date
anoAtual = date.today().year
print(f'O ano atual é {anoAtual}')
anoNascimento = int(input('Informe o ano de nascimento do atleta: '))
idade = anoAtual - anoNascimento
if idade <= 9:
    print(f'O atleta de {idade} anos, está na categoria MIRIM')
elif idade <= 14:
    print(f'O atleta de {idade} anos, está na categoria INFANTIL')
elif idade <= 19:
    print(f'O atleta de {idade} anos, está na categoria JUNIOR')
elif idade <= 20:
    print(f'O atleta de  {idade} anos, está na categoria SÊNIOR')
else:
    print(f'O atleta de {idade} anos, está na categoria MASTER')



