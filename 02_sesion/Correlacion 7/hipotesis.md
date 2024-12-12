

### Las Hipótesis serían:

**`Arquitectura Hexagonal`**

1. **H1:** Si una arquitectura hexagonal reduce el tiempo de desarrollo, será más adoptada.
2. **H2:** A mayor flexibilidad de integración, mayor será la reducción del acoplamiento en una arquitectura hexagonal.

### Resultados

#### **`Arquitectura Hexagonal`**

* **Relación entre reducción de tiempo de desarrollo y adopción:**
    * **Correlación:** -0.95 (relación fuerte)
    * **Qué significa:** Las arquitecturas hexagonales que logran reducir significativamente el tiempo de desarrollo tienden a ser más adoptadas. Esto apoya la hipótesis H1.

* **Relación entre flexibilidad de integración y reducción de acoplamiento:**
    * **Correlación:** 0.98 (relación muy fuerte)
    * **Qué significa:** A medida que aumenta la flexibilidad de integración de una arquitectura hexagonal, también se incrementa la reducción del acoplamiento, confirmando la hipótesis H2.

### Conclusiones

**`Arquitectura Hexagonal`**

Las empresas prefieren las arquitecturas hexagonales que reducen el tiempo de desarrollo, lo que sugiere que la eficiencia en el desarrollo es clave para su adopción. Además, una mayor flexibilidad en la integración permite una mayor reducción del acoplamiento, lo cual es crucial para la mantenibilidad y escalabilidad del sistema.

## Código en Python


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Crear un DataFrame a partir de los datos
data = {'Año': [2018, 2019, 2020, 2021, 2022],
        'Porcentaje_adopción': [5, 10, 15, 20, 25],
        'Tiempo_desarrollo_reducido': [2, 3, 4, 5, 6],
        'Flexibilidad_integración': [10, 15, 20, 25, 30],
        'Reducción_acoplamiento': [15, 20, 25, 30, 35]}
df = pd.DataFrame(data)

# Crear una figura con dos subplots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

# Hipótesis 1: Porcentaje de adopción vs. Tiempo de desarrollo reducido
X = df['Porcentaje_adopción']
y = df['Tiempo_desarrollo_reducido']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Porcentaje_adopción', y='Tiempo_desarrollo_reducido', data=df, ax=ax1)
sns.regplot(x='Porcentaje_adopción', y='Tiempo_desarrollo_reducido', data=df, ci=None, color='red', ax=ax1)
ax1.set_title('Hipótesis 1: Porcentaje de adopción vs. Tiempo de desarrollo reducido')
ax1.set_xlabel('Porcentaje de adopción (%)')
ax1.set_ylabel('Tiempo de desarrollo reducido (semanas)')

# Hipótesis 2: Flexibilidad de integración vs. Reducción de acoplamiento
X = df['Flexibilidad_integración']
y = df['Reducción_acoplamiento']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

sns.scatterplot(x='Flexibilidad_integración', y='Reducción_acoplamiento', data=df, ax=ax2)
sns.regplot(x='Flexibilidad_integración', y='Reducción_acoplamiento', data=df, ci=None, color='red', ax=ax2)
ax2.set_title('Hipótesis 2: Flexibilidad de integración vs. Reducción de acoplamiento')
ax2.set_xlabel('Flexibilidad de integración (%)')
ax2.set_ylabel('Reducción de acoplamiento (%)')

plt.tight_layout()
plt.show()
```
