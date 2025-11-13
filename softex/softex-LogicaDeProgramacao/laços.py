# Exercício que pede para criar uma simulação de contagem regressiva de uma bomba

from time import sleep
print("Iniciando contagem regressiva para a BOMBA!")
for segundos in range(10, 0, -1):
    print(f"{segundos}...", end="")
    sleep(0.9)
print("BUM!.")



