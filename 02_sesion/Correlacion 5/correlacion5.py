import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Crear un DataFrame a partir de los datos
data = {'Año': [2018, 2019, 2020, 2021, 2022],
        'Porcentaje_uso': [30, 35, 45, 50, 60],
        'Tiempo_respuesta': [8, 10, 12, 15, 18],
        'Latencia': [400, 350, 300, 250, 200],
        'Seguridad': [5, 8, 10, 12, 15]}
df = pd.DataFrame(data)

# Crear una figura con dos subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Hipótesis 1: Porcentaje de uso vs. Tiempo de respuesta
X = df['Porcentaje_uso']
y = df['Tiempo_respuesta']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Porcentaje_uso', y='Tiempo_respuesta', data=df, ax=ax1)
sns.regplot(x='Porcentaje_uso', y='Tiempo_respuesta', data=df, ci=None, color='red', ax=ax1)
ax1.set_title('Hipótesis 1: Porcentaje de uso vs. Tiempo de respuesta')
ax1.set_xlabel('Porcentaje de uso en aplicaciones distribuidas (%)')
ax1.set_ylabel('Tiempo de respuesta mejorado (%)')

# Hipótesis 2: Porcentaje de uso vs. Latencia
X = df['Porcentaje_uso']
y = df['Latencia']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Porcentaje_uso', y='Latencia', data=df, ax=ax2)
sns.regplot(x='Porcentaje_uso', y='Latencia', data=df, ci=None, color='red', ax=ax2)
ax2.set_title('Hipótesis 2: Porcentaje de uso vs. Latencia')
ax2.set_xlabel('Porcentaje de uso en aplicaciones distribuidas (%)')
ax2.set_ylabel('Latencia promedio reducida (ms)')

plt.tight_layout()
plt.show()