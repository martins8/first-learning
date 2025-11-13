def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except KeyboardInterrupt:
            n = 0
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return n
        except (ValueError, TypeError):
            print(f'\033[31m ERROR: por favor, digite um número inteiro válido.\033[m')


def leiareal(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except KeyboardInterrupt:
            n = 0
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return n
        except (ValueError, TypeError):
            print(f'\033[31mO ERROR: por favor, digite um número real válido.\033[m')


numero1 = leiaint('Digite um número: ')
numero2 = leiareal('Digite um número: ')
print(f'O número inteiro digitado: {numero1}\n'
      f'O número real digitado: {numero2}')
