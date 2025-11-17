firstTerm = int(input('Diga o primeiro termo da PA: '))
razao = int(input('Diga a razão da PA: '))
print('\n'
      f'{firstTerm}', end=' → ')
consecutivo = firstTerm
for contador in range(1, 10):
    consecutivo += razao
    print(consecutivo, end=' → ')
print('FIM')



