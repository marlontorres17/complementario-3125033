import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Datos en formato CSV
data = """Año,Adopción global (%),Escalabilidad mejorada (%),Reducción de latencia (%),Complejidad de implementación (escala 1-10)
2018,10,20,5,7
2019,15,25,7,6
2020,20,30,10,5
2021,25,35,12,4
2022,30,40,15,3
"""

# Guardar datos en un archivo llamado 'cqrs.csv'
filename = "cqrs.csv"
with open(filename, "w", encoding="utf-8") as file:
    file.write(data)

# Leer datos desde el archivo CSV
try:
    df_cqrs = pd.read_csv(filename)
    print("Datos cargados exitosamente:")
    print(df_cqrs)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

# Configuración para las gráficas
plt.figure(figsize=(15, 12))

# Gráfica 1: Escalabilidad vs. Complejidad (Seaborn con regresión)
plt.subplot(3, 1, 1)
sns.regplot(
    x="Escalabilidad mejorada (%)",
    y="Complejidad de implementación (escala 1-10)",
    data=df_cqrs,
    line_kws={"color": "red"}
)
plt.title("Relación entre Escalabilidad y Complejidad de Implementación")
plt.xlabel("Escalabilidad mejorada (%)")
plt.ylabel("Complejidad de implementación (escala 1-10)")

# Gráfica 2: Reducción de Latencia vs. Adopción Global (Matplotlib dispersión clásica)
plt.subplot(3, 1, 2)
plt.scatter(
    df_cqrs["Adopción global (%)"],
    df_cqrs["Reducción de latencia (%)"],
    c='blue',
    alpha=0.7,
    edgecolors='k'
)
plt.title("Relación entre Adopción Global y Reducción de Latencia")
plt.xlabel("Adopción global (%)")
plt.ylabel("Reducción de latencia (%)")

# Gráfica 3: Escalabilidad vs. Adopción Global (Gráfica con tamaño variable)
plt.subplot(3, 1, 3)
plt.scatter(
    df_cqrs["Adopción global (%)"],
    df_cqrs["Escalabilidad mejorada (%)"],
    s=df_cqrs["Escalabilidad mejorada (%)"] * 10,
    c='green',
    alpha=0.6,
    edgecolors='k'
)
plt.title("Relación entre Adopción Global y Escalabilidad")
plt.xlabel("Adopción global (%)")
plt.ylabel("Escalabilidad mejorada (%)")

# Ajustar el diseño de las gráficas
plt.tight_layout()

# Mostrar las gráficas
plt.show()
