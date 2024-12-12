import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Crear un DataFrame a partir de los datos
data = {'Año': [2018, 2019, 2020, 2021, 2022],
        'Porcentaje_adopción_grandes_empresas': [40, 50, 60, 70, 80],
        'Tiempo_entrega_reducido': [10, 15, 20, 25, 30],
        'Errores_integración_reducidos': [5, 10, 15, 20, 25],
        'Productividad_incrementada': [15, 20, 25, 30, 35]}
df = pd.DataFrame(data)

# Crear una figura con dos subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Hipótesis 1: Porcentaje de adopción en grandes empresas vs. Tiempo de entrega reducido
X = df['Porcentaje_adopción_grandes_empresas']
y = df['Tiempo_entrega_reducido']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Porcentaje_adopción_grandes_empresas', y='Tiempo_entrega_reducido', data=df, ax=ax1)
sns.regplot(x='Porcentaje_adopción_grandes_empresas', y='Tiempo_entrega_reducido', data=df, ci=None, color='red', ax=ax1)
ax1.set_title('Hipótesis 1: Porcentaje de adopción en grandes empresas vs. Tiempo de entrega reducido')
ax1.set_xlabel('Porcentaje de adopción en grandes empresas (%)')
ax1.set_ylabel('Tiempo de entrega reducido (%)')

# Hipótesis 2: Reducción de errores de integración vs. Productividad incrementada
X = df['Errores_integración_reducidos']
y = df['Productividad_incrementada']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Errores_integración_reducidos', y='Productividad_incrementada', data=df, ax=ax2)
sns.regplot(x='Errores_integración_reducidos', y='Productividad_incrementada', data=df, ci=None, color='red', ax=ax2)
ax2.set_title('Hipótesis 2: Reducción de errores de integración vs. Productividad incrementada')
ax2.set_xlabel('Reducción de errores de integración (%)')
ax2.set_ylabel('Productividad incrementada (%)')

plt.tight_layout()
plt.show()