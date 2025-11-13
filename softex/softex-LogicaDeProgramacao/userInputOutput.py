# Faça uma função calculadora que os números e as operações serão feitas
# pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha
# a opção de sair. No início, o programa mostrará a seguinte lista de operações:
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e
# segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado
# na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.
# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.

# Como eu, Arthur Martins, já tinha feito grande parte desse exercício na atividade anterior, irei reaproveitar o código
# e implementar apenas o que falta.

from time import sleep


def usuarioopcoes():
    opcoes = int(input("Escolha a opção númerica referente à ação que deseja realizar (DIGITE O NÚMERO INDICADO)\n"
                       " [ 1 ] Soma\n [ 2 ] Subtração\n [ 3 ] Multiplicação\n [ 4 ] Divisão\n [ 0 ] Sair do programa"
                       "\n Sua escolha: "))
    if opcoes < 0 or opcoes > 4:
        print(f"Essa opção não existe, escolha uma opção válida!")
        usuarioopcoes()
    else:
        return opcoes


def calculadora(n1, n2, op):
    if op == 1:
        result = n1 + n2
        return f"O resultado de {n1} + {n2} é: {result}"
    elif op == 2:
        result = n1 - n2
        return f"O resultado de {n1} - {n2} é: {result}"
    elif op == 3:
        result = n1 * n2
        return f"O resultado de {n1} * {n2} é: {result}"
    elif op == 4:
        result = n1 / n2
        return f"O resultado de {n1} / {n2} é: {result}"


print(f"{'-' * 5}CALCULADORA{f'-' * 5}")

while True:
    opcaoEscolhida = usuarioopcoes()
    if opcaoEscolhida == 0:
        print("Programa Finalizado!")
        break

    else:
        operando1 = int(input("Informe um número: "))
        operando2 = int(input("Informe outro número: "))
        resultado = calculadora(operando1, operando2, opcaoEscolhida)
        print(resultado)
        sleep(1)
