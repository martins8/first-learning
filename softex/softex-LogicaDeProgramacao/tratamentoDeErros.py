# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir
# dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará
# perguntando até que um valor correto seja preenchido.

while True:
    try:
        usuario_nome = str(input("Informe o seu nome completo: "))
        usuario_dataNascimento = int(input("Informe a sua data de nascimento (Que seja entre 1922 e 2021)"))
        if usuario_dataNascimento < 1922 or usuario_dataNascimento > 2021:
            raise Exception("Informe uma data de nascimento Válida")
        else:
            print(f"\nNome do usuário: {usuario_nome}\nData de Nascimento: {usuario_dataNascimento}\n"
                  f"A idade que completou/completará em 2022: {2022-usuario_dataNascimento}")
            print("Programa Finalizado!")
            break

    except Exception as error:
        print("\nERROR")
        print(f"{error}\n")
