import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path1 = "Vendas.csv"
dataset_vendas = pd.read_csv(path1)

path2 = "Produtos.csv"
dataset_produtos = pd.read_csv(path2)


# Formatting the dataset_vendas
dataset_vendas["DATA"] = pd.to_datetime(
    dataset_vendas["DATA"], format="mixed", dayfirst=False
)
dataset_vendas["VALOR_VENDA"] = (
    dataset_vendas["VALOR_VENDA"].str.replace(",", ".").astype(float)
)
dataset_produtos["PREÇO_KG"] = (
    dataset_produtos["PREÇO_KG"].str.replace(",", ".").astype(float)
)



###################################################### Questão 1 ################################################
# Grouping by date
daily_revenue = (
    dataset_vendas.groupby(dataset_vendas["DATA"].dt.date)["VALOR_VENDA"]
    .sum()
    .reset_index()
)
# Plotting the Graph of general evolution
plt.plot(daily_revenue["DATA"], daily_revenue["VALOR_VENDA"], marker="o")
plt.title("Evolução Geral(Todos Os Produtos)")
plt.xlabel("Data")
plt.ylabel("Faturamento (em R$)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#################################################################################################################




###################################################### Questão 2 ################################################
best_day = daily_revenue.loc[daily_revenue["VALOR_VENDA"].idxmax()]
print(f"Melhor dia de vendas foi: {best_day["DATA"]}, com um valor de R${best_day["VALOR_VENDA"]}")
print("\n")
#################################################################################################################



###################################################### Questão 3 ################################################
nome_produto = "Banana"
banana_id = dataset_produtos.loc[
    dataset_produtos["NOME_PRODUTO"] == nome_produto, "ID_PRODUTO"
].values[0]

banana_sales = dataset_vendas[dataset_vendas["ID_PRODUTO"] ==  banana_id]
plt.plot(banana_sales["DATA"], banana_sales["VALOR_VENDA"], marker="o")
plt.title("Evolução Geral(Todos Os Produtos)")
plt.xlabel("Data")
plt.ylabel("Faturamento (em R$)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

best_banana_sales = banana_sales.groupby('DATA')['VALOR_VENDA'].sum().reset_index()
best_banana_day = best_banana_sales.loc[best_banana_sales["VALOR_VENDA"].idxmax()]
print(f"Melhor dia de vendas de {nome_produto} foi: {best_banana_day["DATA"]}, com um valor de R${best_banana_day["VALOR_VENDA"]}")
print("\n")
#################################################################################################################



###################################################### Questão 5 ################################################
vendas_id = dataset_vendas.groupby(dataset_vendas["ID_PRODUTO"])["VALOR_VENDA"].sum().reset_index()
preço_kg = dataset_produtos.groupby(dataset_produtos["ID_PRODUTO"])['PREÇO_KG'].sum().reset_index()

length = len(preço_kg["ID_PRODUTO"])
peso_vendido = {}
max = 0
for i in range(length):
  if(vendas_id["ID_PRODUTO"][i] == preço_kg["ID_PRODUTO"][i]):
    peso_vendido[vendas_id["ID_PRODUTO"][i]] = float(vendas_id["VALOR_VENDA"][i]) / float(preço_kg["PREÇO_KG"][i])

  if(i>=2 and peso_vendido[vendas_id["ID_PRODUTO"][i]] > max):
    max = float(vendas_id["VALOR_VENDA"][i]) / float(preço_kg["PREÇO_KG"][i])
    max_id = i+1


plt.bar(*zip(*peso_vendido.items()))
plt.xticks(np.arange(1,length+1,1))
plt.show()
print(f"Produto com ID:{max_id} foi o que mais foi vendido, vendendo {max} Kg")
#################################################################################################################
