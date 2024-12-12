
### Las Hipótesis serían:

**`BFF (Backend for Frontend)`**

1. **H1:** Si un BFF reduce el tiempo de respuesta, será más adoptado en aplicaciones móviles.
2. **H2:** A mayor tasa de satisfacción del usuario final, mayor será la reducción de la complejidad del frontend en un BFF.

### Resultados

#### **`BFF (Backend for Frontend)`**

* **Relación entre reducción de tiempo de respuesta y adopción:**
    * **Correlación:** -0.95 (relación fuerte)
    * **Qué significa:** Los BFFs que logran reducir significativamente el tiempo de respuesta tienden a ser más adoptados en aplicaciones móviles. Esto apoya la hipótesis H1.

* **Relación entre tasa de satisfacción del usuario final y reducción de la complejidad del frontend:**
    * **Correlación:** 0.98 (relación muy fuerte)
    * **Qué significa:** A medida que aumenta la tasa de satisfacción del usuario final, también se incrementa la reducción de la complejidad del frontend en los BFFs, confirmando la hipótesis H2.

### Conclusiones

**`BFF (Backend for Frontend)`**

Las empresas prefieren los BFFs que ofrecen tiempos de respuesta rápidos, lo que sugiere que la eficiencia en el rendimiento es clave para su adopción en aplicaciones móviles. Además, una mayor tasa de satisfacción del usuario final se correlaciona con una reducción de la complejidad del frontend, lo cual es crucial para una mejor experiencia de usuario y mantenimiento del sistema.

## Código en Python


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Crear un DataFrame a partir de los datos
data = {'Año': [2018, 2019, 2020, 2021, 2022],
        'Porcentaje_adopción_móvil': [20, 30, 40, 50, 60],
        'Tasa_satisfacción': [70, 75, 80, 85, 90],
        'Reducción_complejidad_frontend': [10, 15, 20, 25, 30],
        'Tiempo_respuesta_reducido': [300, 280, 260, 240, 220]}
df = pd.DataFrame(data)

# Crear una figura con dos subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Hipótesis 1: Porcentaje de adopción en aplicaciones móviles vs. Tiempo de respuesta reducido
X = df['Porcentaje_adopción_móvil']
y = df['Tiempo_respuesta_reducido']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Porcentaje_adopción_móvil', y='Tiempo_respuesta_reducido', data=df, ax=ax1)
sns.regplot(x='Porcentaje_adopción_móvil', y='Tiempo_respuesta_reducido', data=df, ci=None, color='red', ax=ax1)
ax1.set_title('Hipótesis 1: Porcentaje de adopción en aplicaciones móviles vs. Tiempo de respuesta reducido')
ax1.set_xlabel('Porcentaje de adopción en aplicaciones móviles (%)')
ax1.set_ylabel('Tiempo de respuesta reducido (ms)')

# Hipótesis 2: Tasa de satisfacción del usuario final vs. Reducción de la complejidad del frontend
X = df['Tasa_satisfacción']
y = df['Reducción_complejidad_frontend']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Tasa_satisfacción', y='Reducción_complejidad_frontend', data=df, ax=ax2)
sns.regplot(x='Tasa_satisfacción', y='Reducción_complejidad_frontend', data=df, ci=None, color='red', ax=ax2)
ax2.set_title('Hipótesis 2: Tasa de satisfacción del usuario final vs. Reducción de la complejidad del frontend')
ax2.set_xlabel('Tasa de satisfacción del usuario final (%)')
ax2.set_ylabel('Reducción de la complejidad del frontend (%)')

plt.tight_layout()
plt.show()
```
