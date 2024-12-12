import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datoa
df_micro = pd.read_csv('microservicios.csv')
df_eventos = pd.read_csv('diseno_eventos.csv')

# Gráficas de dispersión
plt.figure(figsize=(15, 10))

# Microservicios: Tiempo vs. Adopción en empresas grandes
plt.subplot(2, 2, 1)
sns.regplot(x="Tiempo de implementación promedio (meses)", 
            y="Adopción en empresas grandes (%)", 
            data=df_micro, 
            line_kws={"color": "red"})
plt.title("Microservicios: Tiempo vs Adopción en Empresas Grandes")
plt.xlabel("Tiempo de implementación promedio (meses)")
plt.ylabel("Adopción en empresas grandes (%)")

# Microservicios: Costo vs. Adopción en empresas grandes
plt.subplot(2, 2, 2)
sns.regplot(x="Costo de implementación promedio (USD)", 
            y="Adopción en empresas grandes (%)", 
            data=df_micro, 
            line_kws={"color": "red"})
plt.title("Microservicios: Costo vs Adopción en Empresas Grandes")
plt.xlabel("Costo de implementación promedio (USD)")
plt.ylabel("Adopción en empresas grandes (%)")

# Diseño basado en eventos: Adopción global vs. Aumento de rendimiento
plt.subplot(2, 2, 3)
sns.regplot(x="Adopción global (%)", 
            y="Aumento de rendimiento (%)", 
            data=df_eventos, 
            line_kws={"color": "blue"})
plt.title("Diseño Basado en Eventos: Adopción Global vs Aumento de Rendimiento")
plt.xlabel("Adopción global (%)")
plt.ylabel("Aumento de rendimiento (%)")

# Diseño basado en eventos: Eventos manejados vs. Reducción de tiempo de respuesta
plt.subplot(2, 2, 4)
sns.regplot(x="Eventos manejados por segundo (media)", 
            y="Reducción de tiempo de respuesta (%)", 
            data=df_eventos, 
            line_kws={"color": "blue"})
plt.title("Diseño Basado en Eventos: Eventos Manejados vs Reducción de Tiempo")
plt.xlabel("Eventos manejados por segundo (media)")
plt.ylabel("Reducción de tiempo de respuesta (%)")

plt.tight_layout()
plt.show()
