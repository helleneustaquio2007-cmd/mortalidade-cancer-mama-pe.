PYTHON
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
#1. Carregar o arquivo CSV do DATASUS pulando o cabeçalho descritivo
file_path = "sim_cnv_obt10pe171236168_196_221_49.csv"
df = pd.read_csv(file_path, encoding="latin1", sep=";", skiprows=5) 

#2. Limpeza básica dos dados
# Remover linhas nulas no final (como notas de rodapé do DATASUS)
df = df.dropna(subset=["Município"])

# AS Colunas de faixa etária usam '_' para indicar zero óbitos. Vamos substituir por '0' e converter para inteiro
age_columns = [

    "15 a 19 anos",
    "20 a 29 anos",
    "30 a 39 anos",
    "40 a 49 anos",
    "50 a 59 anos",
    "60 a 69 anos",
    "70 a 79 anos",
    "80 anos e mais",
    "Idade Ignorada".
]
for col in age_columns:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace("_", "0"), errors="coerce").fillna(0)

    #Garantir que a coluna total seja numérica
    df["Total"] = pd.to_numeric(df["Total"], errors="coerce"). fillna(0)

    #3. Exibir um resumo estatístico geral dos óbitos por município
    print("--- Resumo Estatístico dos Totais por Município ---")
    print(df["Total"].describe())

    # 4. Encontrar o município com o maior número de óbitos no período
    top_municipios = df.sort_values(by="Total", ascending=False).head(5)
    print("\n--- Top 5 Municípiot com Mais Óbitos ---")
    print(top_municipios[["Município", "Total"]])")

    # 5. Somar os óbitos por faixa etária em todo o estado para visualizar a distribuição
    total_por_faixa = df[age_columns].sum() 
    print("\n--- Óbitos por Faixa Etária (Pernambuco 2020-2024)---")
    print(total_por_faixa)





