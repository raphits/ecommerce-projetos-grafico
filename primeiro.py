import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do arquivo
df = pd.read_csv('/Users/tamilalima/Downloads/ecommerce_preparados.csv')

# Tratamento dos dados
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce').fillna(0)
df['Marca'] = df['Marca'].astype('category').cat.codes

#grafico de histograma
plt.figure(figsize=(10,6))
plt.hist(df['Qtd_Vendidos'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição da Quantidade de Vendas')
plt.xlabel('Quantidade de Vendas')
plt.ylabel('Frequência')
plt.show()

#grafico de dispersao

plt.figure(figsize=(10,6))
plt.scatter(df['N_Avaliações'], df['Qtd_Vendidos'], alpha=0.6, color='purple')
plt.title('Dispersão entre Avaliações e Quantidade de Vendas')
plt.xlabel('Número de Avaliações')
plt.ylabel('Quantidade de Vendas')
plt.show()

#mapa de calor

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor - Correlação entre Variáveis')
plt.show()

#grafico de barras

plt.figure(figsize=(10,6))
top5_marcas = df['Marca'].value_counts().head(5)
top5_marcas.plot(kind='bar', color='orange')
plt.title('Top 5 Marcas com Mais Produtos')
plt.xlabel('Marca')
plt.ylabel('Quantidade de Produtos')
plt.xticks(rotation=0)
plt.show()

#grafico de pizza

avaliacoes_top5 = df['N_Avaliações'].value_counts().head(5)
plt.figure(figsize=(8,8))
plt.pie(avaliacoes_top5.values, labels=avaliacoes_top5.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição das Top 5 Avaliações')
plt.show()

#grafico de densidade

plt.figure(figsize=(10,6))
sns.kdeplot(df['Qtd_Vendidos'], fill=True, color='green')
plt.title('Distribuição de Densidade da Quantidade de Vendas')
plt.xlabel('Quantidade de Vendas')
plt.show()

#grafico de regressao

plt.figure(figsize=(10,6))
sns.regplot(x='N_Avaliações', y='Qtd_Vendidos', data=df, color='blue', scatter_kws={'alpha': 0.5})
plt.title('Regressão entre Avaliações e Vendas')
plt.xlabel('Número de Avaliações')
plt.ylabel('Quantidade de Vendas')
plt.show()