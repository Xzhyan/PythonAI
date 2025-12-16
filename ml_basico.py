import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# =========================
# 1️⃣ CRIANDO OS DADOS
# =========================

idades = np.array([18, 20, 22, 25, 30, 35, 40])
salarios = np.array([1200, 1500, 1800, 2500, 3500, 4200, 5000])

# Criando o DataFrame
df = pd.DataFrame({
    "idade": idades,
    "salario": salarios
})

print("=== DATASET ===")
print(df)

# =========================
# 2️⃣ VISUALIZAÇÃO DOS DADOS
# =========================

plt.scatter(df["idade"], df["salario"])
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.title("Idade x Salário")
plt.show()

# =========================
# 3️⃣ PREPARAÇÃO PARA ML
# =========================

# Feature (X) e Label (y)
X = df[["idade"]]   # precisa ser 2D
y = df["salario"]   # pode ser 1D

# =========================
# 4️⃣ CRIANDO E TREINANDO O MODELO
# =========================

modelo = LinearRegression()
modelo.fit(X, y)

# =========================
# 5️⃣ FAZENDO PREVISÃO
# =========================

idade_teste = np.array([[28]])
salario_previsto = modelo.predict(idade_teste)

print("\n=== PREVISÃO ===")
print(f"Salário previsto para 28 anos: R$ {salario_previsto[0]:.2f}")

# =========================
# 6️⃣ VISUALIZANDO A RETA DA REGRESSÃO
# =========================

# Gera idades contínuas para desenhar a reta
idades_linha = np.linspace(df["idade"].min(), df["idade"].max(), 100).reshape(-1, 1)
salarios_linha = modelo.predict(idades_linha)

plt.scatter(df["idade"], df["salario"], label="Dados reais")
plt.plot(idades_linha, salarios_linha, label="Reta da regressão")
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.title("Regressão Linear - Idade x Salário")
plt.legend()
plt.show()
