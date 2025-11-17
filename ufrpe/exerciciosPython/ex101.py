def voto(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


votar = int(input('Em que ano você nasceu? '))
print(voto(votar))

