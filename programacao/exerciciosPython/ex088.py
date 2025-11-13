from random import randint
from time import sleep
print(f'{"=" * 40}\n'
      f'{"JOGA NA MEGA SENA":^40}\n'
      f'{"=" * 40}')
qntdJogos = int(input('Quantos jogos quer que eu sorteie? '))
megasena = [[] for contador in range(0, qntdJogos)]
print(f'{"-="*3} {"SORTEANDO JOGOS"} {"-="*3}')
for jogos in range(0, len(megasena)):
    for numeros in range(1, 7):
        numeroAleatorio = randint(1, 60)
        if numeroAleatorio not in megasena[jogos]:
            megasena[jogos].append(numeroAleatorio)
for posicao, jogos in enumerate(megasena):
    print(f'Jogo {posicao+1}: {jogos}')
    sleep(0.5)



