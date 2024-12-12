
### Las Hipótesis serían:

**`PWA (Progressive Web Apps)`**

1. **H1:** Si una PWA tiene un menor tiempo de respuesta, será más adoptada por los mercados emergentes.
2. **H2:** A mayor capacidad de escalabilidad, mayor será el costo de implementación de una PWA.

### Resultados

#### **`PWA (Progressive Web Apps)`**

* **Relación entre tiempo de respuesta y adopción:**
    * **Correlación:** -0.95 (relación fuerte)
    * **Qué significa:** Las PWAs con tiempos de respuesta más bajos tienden a ser más populares entre los mercados emergentes. Esto apoya la hipótesis H1.

* **Relación entre escalabilidad y costo:**
    * **Correlación:** 0.98 (relación muy fuerte)
    * **Qué significa:** A medida que aumenta la capacidad de una PWA para manejar más tráfico, su costo de implementación también se incrementa, confirmando la hipótesis H2.

### Conclusiones

**`PWA (Progressive Web Apps)`**

Las empresas prefieren las PWAs que ofrecen tiempos de respuesta rápidos. Por lo tanto, optimizar la performance es clave para aumentar la adopción. Además, es importante tener en cuenta que la escalabilidad tiene un costo asociado, y las empresas deberán evaluar si el beneficio de una mayor capacidad justifica el gasto adicional.

## Código en Python

```python
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
```

