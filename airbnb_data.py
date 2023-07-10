# Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Lendo arquivo
df = pd.read_csv('caminho/do/arquivo.csv')

# Verificar as primeiras linhas do DataFrame
print(df.head())

# Obter informações gerais sobre o DataFrame
print(df.info())

# Calcular estatísticas descritivas dos dados numéricos
print(df.describe())

# Media Preçoes alugueis
media_precos = df['preco'].mean()
print(f"Média de preços dos aluguéis: {media_precos:.2f}")

# Bairros populares
bairros_populares = df['bairro'].value_counts()
print("Bairros mais populares:")
print(bairros_populares)

precos_medios_por_bairro = df.groupby('bairro')['preco'].mean()
precos_medios_por_bairro.plot(kind='bar')
plt.xlabel('Bairro')
plt.ylabel('Preço Médio')
plt.title('Preço Médio dos Aluguéis por Bairro')
plt.show()
