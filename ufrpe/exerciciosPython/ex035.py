
print("""                   VERIFICADOR DE TRIÂNGULO
Informe os valores de três retas para sabermos se com tais valores
um triângulo pode ser formato\n  """)

reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Com os valores citados, pode-se formar um triângulo')
else:
    print('Com os valores citados, não é possível formar um triângulo')





