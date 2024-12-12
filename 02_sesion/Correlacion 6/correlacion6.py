import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Crear un DataFrame a partir de los datos
data = {'Año': [2018, 2019, 2020, 2021, 2022],
        'Adopción_mercados_emergentes': [10, 20, 30, 40, 50],
        'Adopción_mercados_desarrollados': [15, 25, 35, 45, 55],
        'Usuarios_recurrentes': [30, 35, 40, 45, 50],
        'Aumento_tráfico_móvil': [5, 10, 15, 20, 25]}
df = pd.DataFrame(data)

# Crear una figura con dos subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Hipótesis 1: Adopción en mercados emergentes vs. Adopción en mercados desarrollados
X = df['Adopción_mercados_emergentes']
y = df['Adopción_mercados_desarrollados']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Adopción_mercados_emergentes', y='Adopción_mercados_desarrollados', data=df, ax=ax1)
sns.regplot(x='Adopción_mercados_emergentes', y='Adopción_mercados_desarrollados', data=df, ci=None, color='red', ax=ax1)
ax1.set_title('Hipótesis 1: Adopción en mercados emergentes vs. Adopción en mercados desarrollados')
ax1.set_xlabel('Adopción en mercados emergentes (%)')
ax1.set_ylabel('Adopción en mercados desarrollados (%)')

# Hipótesis 2: Adopción en mercados emergentes vs. Usuarios recurrentes
X = df['Adopción_mercados_emergentes']
y = df['Usuarios_recurrentes']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Adopción_mercados_emergentes', y='Usuarios_recurrentes', data=df, ax=ax2)
sns.regplot(x='Adopción_mercados_emergentes', y='Usuarios_recurrentes', data=df, ci=None, color='red', ax=ax2)
ax2.set_title('Hipótesis 2: Adopción en mercados emergentes vs. Usuarios recurrentes')
ax2.set_xlabel('Adopción en mercados emergentes (%)')
ax2.set_ylabel('Usuarios recurrentes (%)')

plt.tight_layout()
plt.show()
