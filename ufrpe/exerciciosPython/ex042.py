# Ao receber trÊs valores referentes a uma reta qualquer, analisa tais retas e checa se com elas pode-se formar um
# triângulo. Após isso, será verificado o tipo de triângulo obtido com os valores informados.
print('ANALISADOR DE TRIÂNGULOS')
reta1 = float(input('Informe o valor da primeira reta: '))
reta2 = float(input('Informe o valor da segunda reta: '))
reta3 = float(input('Informe o valor da terceira reta: '))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('Com tais valores será possível formar um triângulo')
    if reta1 == reta2 == reta3:
        print('O triângulo formado será EQUILATERO')
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('O triângulo formado será ISÓSCELES')
    else:
        print('O triângulo formado será ESCALENO')
else:
    print('Com tais valores de retas não é possível formar um triângulo')
