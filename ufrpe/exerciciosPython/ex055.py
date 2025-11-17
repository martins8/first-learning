maiorMassa = 0
menorMassa = 0
for contador in range(1, 6):
    massa = float(input('Informe a sua massa em KG: '))
    if massa > maiorMassa:
        maiorMassa = massa
    if contador == 1:
        menorMassa = massa
    elif massa < menorMassa:
        menorMassa = massa
print(f'A maior massa obtida foi de {maiorMassa}Kg\n'
      f'A menor massa obtida foi de {menorMassa}Kg')




