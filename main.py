import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dados simples
idades = np.array([18, 20, 22, 24, 30, 34, 40])
salarios = np.array([1200, 1500, 1800, 2000, 3000, 4000, 5000])

# criando um data frame
df = pd.DataFrame({
    "idade": idades,
    "salario": salarios,
})

print(df)

# plotando os dados
plt.scatter(df["idade"], df["salario"])
plt.xlabel("Idade")
plt.ylabel("Salário")
plt.title("Idade x Salário")
plt.show()