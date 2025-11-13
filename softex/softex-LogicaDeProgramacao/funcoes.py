# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação
# e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:

# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

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
    else:
        result = 0
        return f"Visto que você não informou nenhuma opção válide\n para relizar alguma operação" \
               f"o resultado será: {result}"


print(f"{'-'*5}CALCULADORA{f'-'*5}")
operando1 = int(input("Informe um número: "))
operando2 = int(input("Informe outro número: "))
operador = int(input("Qual operador desejará usar:(DIGITE O NÚMERO INDICADO)\n"
                     " [ 1 ] Soma\n [ 2 ] Subtração\n [ 3 ] Multiplicação\n [ 4 ] Divisão\n"
                     "Sua escolha: "))
resultado = calculadora(operando1, operando2, operador)
print(resultado)

