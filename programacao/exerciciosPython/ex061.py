firstTerm = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Digite a razão desejada para a PA: '))
contador = 1
otherTerms = firstTerm
print(firstTerm, end='')
while contador != 10:
    otherTerms += razao
    print(f' → {otherTerms}', end='')
    contador += 1









