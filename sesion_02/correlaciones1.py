import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datos: Microservicios
data_micro = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Adopción en empresas medianas (%)": [35, 45, 55, 60, 70],
    "Adopción en empresas grandes (%)": [40, 50, 65, 70, 80],
    "Tiempo de implementación promedio (meses)": [9, 8, 7, 6, 5],
    "Costo de implementación promedio (USD)": [120000, 115000, 110000, 105000, 100000],
}

# Datos: Diseño basado en eventos
data_eventos = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Adopción global (%)": [25, 30, 35, 40, 50],
    "Eventos manejados por segundo (media)": [1000, 1200, 1500, 1800, 2000],
    "Reducción de tiempo de respuesta (%)": [10, 12, 15, 18, 20],
    "Aumento de rendimiento (%)": [5, 8, 10, 12, 15],
}

# Crear DataFrames
df_micro = pd.DataFrame(data_micro)
df_eventos = pd.DataFrame(data_eventos)

# Correlaciones para Microservicios
correlation_micro = df_micro.corr()

# Correlaciones para Diseño basado en eventos
correlation_eventos = df_eventos.corr()

# Graficar heatmaps
plt.figure(figsize=(12, 5))

# Heatmap Microservicios
plt.subplot(1, 2, 1)
sns.heatmap(correlation_micro, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlaciones: Microservicios")

# Heatmap Diseño basado en eventos
plt.subplot(1, 2, 2)
sns.heatmap(correlation_eventos, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlaciones: Diseño Basado en Eventos")

plt.tight_layout()
plt.show()
