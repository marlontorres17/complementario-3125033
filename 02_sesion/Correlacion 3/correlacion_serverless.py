import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Datos para el archivo CSV
data = """Año,Porcentaje de adopción en aplicaciones nuevas (%),Costos operativos reducidos (%),Tiempo de respuesta medio (ms),Escalabilidad dinámica (%)
2018,20,15,500,50
2019,25,20,450,55
2020,35,25,400,60
2021,40,30,350,65
2022,50,35,300,70
"""

# Nombre del archivo CSV
filename = "serverless.csv"

# Crear el archivo CSV
with open(filename, "w", encoding="utf-8") as file:
    file.write(data)

# Leer el archivo CSV
try:
    df_serverless = pd.read_csv(filename, encoding="utf-8")
    print("Datos cargados exitosamente:")
    print(df_serverless)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

# Configuración para las gráficas
plt.figure(figsize=(12, 8))

# Gráfica 1: Dispersión con líneas de regresión (Seaborn)
plt.subplot(2, 1, 1)
sns.regplot(
    x="Costos operativos reducidos (%)", 
    y="Porcentaje de adopción en aplicaciones nuevas (%)", 
    data=df_serverless, 
    line_kws={"color": "red"}
)
plt.title("Relación entre costos operativos y adopción de serverless")
plt.xlabel("Costos operativos reducidos (%)")
plt.ylabel("Adopción en aplicaciones nuevas (%)")

# Gráfica 2: Dispersión con tamaño de puntos variable (Matplotlib)
plt.subplot(2, 1, 2)
plt.scatter(
    df_serverless["Tiempo de respuesta medio (ms)"], 
    df_serverless["Escalabilidad dinámica (%)"], 
    s=df_serverless["Porcentaje de adopción en aplicaciones nuevas (%)"] * 10, 
    alpha=0.7, 
    c='blue', 
    edgecolors='k'
)
plt.title("Relación entre tiempo de respuesta y escalabilidad dinámica")
plt.xlabel("Tiempo de respuesta medio (ms)")
plt.ylabel("Escalabilidad dinámica (%)")

# Ajustar el diseño de las gráficas
plt.tight_layout()

# Mostrar las gráficas
plt.show()
