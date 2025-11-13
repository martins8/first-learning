import ex115listagem
import ex115MENU
import ex115cadastrar

while True:
    ex115MENU.menu()
    options = int(input(f'Sua opção: '))
    if options == 1:
        ex115listagem.showregistereds()
    elif options == 2:
        ex115cadastrar.cadastro()
    elif options == 3:
        print(f'Obrigado pela utilização!')
        break
    else:
        print(f'\033[31mERROR, digite uma opção válida!\033[m')


