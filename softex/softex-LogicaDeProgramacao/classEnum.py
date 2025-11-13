# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0

# O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a
# nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número,
# o código deve retornar uma mensagem para votar novamente.

# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também,
# a quantidade de votos de cada candidato, os brancos e nulos

import enum
from time import sleep


class Eleicao(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0


class QuantidadeVotos:
    branco = 0
    candidato_X = 0
    candidato_Y = 0
    candidato_Z = 0
    nulo = 0


def votar(numero_voto):
    if numero_voto == Eleicao.candidato_X.value:
        QuantidadeVotos.candidato_X += 1
    elif numero_voto == Eleicao.candidato_Y.value:
        QuantidadeVotos.candidato_Y += 1
    elif numero_voto == Eleicao.candidato_Z.value:
        QuantidadeVotos.candidato_Z += 1
    elif numero_voto == Eleicao.branco.value:
        QuantidadeVotos.branco += 1
    else:
        QuantidadeVotos.nulo += 1


def opcoes():
    print("\nELEIÇÃO\n"
          "Digite, corretamente, o número referente ao seu Candidato:\n"
          "\n Candidato X: 889\n Candidato Y: 847\n Candidato Z: 515\n Voto em Branco: 0")
    while True:
        try:
            voto_usuario = int(input("Digite o Nº do seu Candidato a seguir -> "))
            return voto_usuario
        except:
            print("Você inseriu um texto ao invés do número do seu voto, por favor, repita o processo e informe"
                  "os dados corretamente!")


def resultadofinal():
    if QuantidadeVotos.candidato_X > QuantidadeVotos.candidato_Y and QuantidadeVotos.candidato_X > \
            QuantidadeVotos.candidato_Z:
        return "Candidato X"
    elif QuantidadeVotos.candidato_Y > QuantidadeVotos.candidato_X and QuantidadeVotos.candidato_Y > \
            QuantidadeVotos.candidato_Z:
        return "Candidato Y"
    else:
        return "Candidato Z"


while True:
    voto = opcoes()
    sleep(0.5)
    votar(voto)
    finalizar_votacao = str(input("\nDeseja finalizar a votação? [ S ] / [ N ]\n Sua escolha: ")).strip().upper()
    if finalizar_votacao == "S":
        print("Votação FINALIZADA!")
        break

ganhador = resultadofinal()
print(f"\nRESULTADO DA VOTAÇÃO\n"
      f"Votos em Branco: {QuantidadeVotos.branco}\n"
      f"Candidato X: {QuantidadeVotos.candidato_X} voto(s)\n"
      f"Candidato Y: {QuantidadeVotos.candidato_Y} voto(s)\n"
      f"Candidato Z: {QuantidadeVotos.candidato_Z} voto(s)\n"
      f"Nulos: {QuantidadeVotos.nulo}"
      f"\nVENCEDOR: {ganhador}")



