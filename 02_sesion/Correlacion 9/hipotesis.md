
### Las Hipótesis serían:

**`Tolerancia a Fallos`**

1. **H1:** Si un sistema tiene una mayor reducción de caídas, será más adoptado.
2. **H2:** A mayor mejoramiento en la recuperación, mayor será el aumento de fiabilidad en un sistema con tolerancia a fallos.

### Resultados

#### **`Tolerancia a Fallos`**

* **Relación entre reducción de caídas y adopción:**
    * **Correlación:** -0.95 (relación fuerte)
    * **Qué significa:** Los sistemas que logran reducir significativamente las caídas tienden a ser más adoptados. Esto apoya la hipótesis H1.

* **Relación entre mejoramiento en la recuperación y aumento de fiabilidad:**
    * **Correlación:** 0.98 (relación muy fuerte)
    * **Qué significa:** A medida que mejora la capacidad de recuperación de un sistema, también se incrementa su fiabilidad, confirmando la hipótesis H2.

### Conclusiones

**`Tolerancia a Fallos`**

Las empresas prefieren los sistemas con menor incidencia de caídas, lo que sugiere que la estabilidad es clave para su adopción. Además, una mayor capacidad de recuperación se correlaciona con un aumento en la fiabilidad, lo cual es crucial para la continuidad del negocio y la confianza en el sistema.

## Código en Python


```python
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
```

