# Crie um tipo abstrato de dado (TAD) para
# manipular números complexos na linguagem Python.
# O método deve:

# - calcular três números complexos;
# - realizar todas as operações básicas;
# - e imprimir as propriedades real e img do números.

class Ncomplexos:
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3


numeros_complexos = []
for c in range(1, 4):
    vetor = []
    real = float(input(f"Informe a parte real do número {c}: "))
    vetor.append(real)
    img = float(input(f"Informe a parte imaginária do número {c}: "))
    vetor.append(img)
    numeros_complexos.append(vetor)

numero1 = complex(numeros_complexos[0][0], numeros_complexos[0][1])
numero2 = complex(numeros_complexos[1][0], numeros_complexos[1][1])
numero3 = complex(numeros_complexos[2][0], numeros_complexos[2][1])


operacoes = ['+', '-', '*', '/']
for c in range(0, 4):
    if c == 0:
        print(f"{numero1} {operacoes[c]} {numero2} {operacoes[c]} {numero3} = {numero1 + numero2 + numero3}")
    elif c == 1:
        print(f"{numero1} {operacoes[c]} {numero2} {operacoes[c]} {numero3} = {numero1 - numero2 - numero3}")
    elif c == 2:
        print(f"{numero1} {operacoes[c]} {numero2} {operacoes[c]} {numero3} = {numero1 * numero2 * numero3}")
    elif c == 3:
        print(f"{numero1} {operacoes[c]} {numero2} {operacoes[c]} {numero3} = {numero1 / numero2 / numero3}")


