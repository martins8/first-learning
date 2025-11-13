import pandas as pd

arquivo_csv = pd.read_csv("notas-alunos.csv", sep=";")
arquivo_csv["media"] = (arquivo_csv["nota-1"]+arquivo_csv["nota-2"]) / 2

arquivo_csv.loc[arquivo_csv["media"] < 7, "situacao"] = "REPROVADO"
arquivo_csv.loc[arquivo_csv["media"] >= 7, "situacao"] = "APROVADO"
arquivo_csv.loc[arquivo_csv["faltas"] > 5, "situacao"] = "REPROVADO"

arquivo_csv.to_csv("alunos_situacao.csv", sep=";")

print(f"Média geral: {arquivo_csv['media'].median()}")
print(f"Maior média: {arquivo_csv['media'].max()}")
print(f"Maior número de faltas:  {arquivo_csv['faltas'].max()}")


