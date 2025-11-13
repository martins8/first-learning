# ficou com um bug no final.
expressao = str(input('Digite a expressão: '))
listaParenteses = []
fechada = False
pilha = 0
for caracteres in expressao:
    if caracteres == '(' and fechada is False:
        listaParenteses.append(caracteres)
        fechada = True
        pilha += 1
    elif caracteres == ')' and fechada is True:
        listaParenteses.append(caracteres)
        pilha -= 1
        fechada = False
print(listaParenteses)
if pilha == 0:
    print(f'Expressão válida')
else:
    print(f'Expressão inválida')
