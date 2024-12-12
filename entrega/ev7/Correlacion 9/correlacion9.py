import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Crear un DataFrame a partir de los datos
data = {'Año': [2018, 2019, 2020, 2021, 2022],
        'Porcentaje_adopción': [15, 20, 25, 30, 35],
        'Reducción_caídas': [10, 15, 20, 25, 30],
        'Mejoramiento_recuperación': [5, 10, 15, 20, 25],
        'Aumento_fiabilidad': [20, 25, 30, 35, 40]}
df = pd.DataFrame(data)

# Crear una figura con dos subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Hipótesis 1: Porcentaje de adopción vs. Reducción de caídas del sistema
X = df['Porcentaje_adopción']
y = df['Reducción_caídas']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Porcentaje_adopción', y='Reducción_caídas', data=df, ax=ax1)
sns.regplot(x='Porcentaje_adopción', y='Reducción_caídas', data=df, ci=None, color='red', ax=ax1)
ax1.set_title('Hipótesis 1: Porcentaje de adopción vs. Reducción de caídas del sistema')
ax1.set_xlabel('Porcentaje de adopción (%)')
ax1.set_ylabel('Reducción de caídas del sistema (%)')

# Hipótesis 2: Mejoramiento en la recuperación vs. Aumento de fiabilidad
X = df['Mejoramiento_recuperación']
y = df['Aumento_fiabilidad']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Mejoramiento_recuperación', y='Aumento_fiabilidad', data=df, ax=ax2)
sns.regplot(x='Mejoramiento_recuperación', y='Aumento_fiabilidad', data=df, ci=None, color='red', ax=ax2)
ax2.set_title('Hipótesis 2: Mejoramiento en la recuperación vs. Aumento de fiabilidad')
ax2.set_xlabel('Mejoramiento en la recuperación (%)')
ax2.set_ylabel('Aumento de fiabilidad (%)')

plt.tight_layout()
plt.show()