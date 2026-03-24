import pandas as pd

# Criando dados fictícios de vendas
dados = {
    'Produto': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Quantidade': [10, 15, 7, 20, 5, 12],
    'Preco': [100, 150, 200, 100, 150, 200]
}

# Criando DataFrame
df = pd.DataFrame(dados)

# Exibindo os dados
print("Dados de vendas:")
print(df)
print("\n")

# Criando coluna de faturamento
df['Faturamento'] = df['Quantidade'] * df['Preco']

# Análise
faturamento_total = df['Faturamento'].sum()
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()

# Exibindo resultados
print("Faturamento total:", faturamento_total)
print("Produto mais vendido:", produto_mais_vendido)
