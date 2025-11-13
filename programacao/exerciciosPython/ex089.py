coletaNomes = []
coletaNotas = []
listaCompleta = []
while True:
    coletaNomes.append(str(input('Nome: ')))
    for contagem in range(0, 2):
        coletaNotas.append(float(input(f'Nota {contagem+1}: ')))
    coletaNomes.append(coletaNotas[:])
    listaCompleta.append(coletaNomes[:])
    coletaNomes.clear()
    coletaNotas.clear()
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] ')).strip()
    if resposta in 'Nn':
        break
print(f'{"="*30}\n'
      f'No.  NOME{" ":>15} MÉDIA\n'
      f'{"="*30}')
for posicao, alunos in enumerate(listaCompleta):
    print(f'{posicao}    {alunos[0]:<20} {(alunos[1][0] + alunos[1][1]) / 2:.1f}')
print(f'{"="*30}')
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('PROGRAMA FINALIZADO!')
        break
    print(f'Notas de {listaCompleta[opcao][0]} são {listaCompleta[opcao][1]}')











