
---

### Análisis de `Microservicios` y `Diseño Basado en Eventos`  

Estamos viendo cómo los microservicios y el diseño basado en eventos están ayudando en la tecnología. Usamos gráficas y números para entender si hay relaciones entre cosas importantes y si lo que pensamos tiene sentido o no.  

**¿Qué es la correlación?**  
Es una forma de saber si dos cosas tienen que ver entre sí.  
- **Va de -1 a 1**:  
  - Si es -1, cuando una cosa sube, la otra baja.  
  - Si es 1, las dos suben juntas.  
  - Si es 0, no se llevan para nada.  

**Gráficas de dispersión con líneas:**  
Son dibujitos que muestran puntos en un gráfico para ver si algo tiene una tendencia (como si las cosas suben o bajan juntas).  

---

### Las Hipotesis serian:  

**`Microservicios:`**  
1. **H1**: Si toma menos tiempo ponerlos en marcha, las empresas grandes los usan más.  
2. **H2**: Si son más baratos, más empresas los adoptan.  

**`Diseño basado en eventos:`**  
1. **H3**: Si más empresas lo usan, los sistemas funcionan mejor.  
2. **H4**: Si manejan más eventos al mismo tiempo, los sistemas responden más rápido.  

---

### Resultados  

#### **`Microservicios`**  
- **Relación entre tiempo y uso:**  
  - **Correlación:** -0.99 (relación súper fuerte).  
  - **Qué significa:** Cuando toma menos meses implementarlos, más empresas los usan. Esto hace que H1 sea cierta.  

- **Relación entre costo y uso:**  
  - **Correlación:** -0.99 (también súper fuerte).  
  - **Qué significa:** Si son más baratos, más empresas los adoptan. Esto confirma H2.  

#### **`Diseño Basado en Eventos`**  
- **Relación entre uso global y rendimiento:**  
  - **Correlación:** 0.99 (relación muy fuerte).  
  - **Qué significa:** Mientras más empresas lo adoptan, los sistemas funcionan mucho mejor. Esto hace que H3 sea correcta.  

- **Relación entre eventos por segundo y respuesta rápida:**  
  - **Correlación:** 1.00 (relación perfecta).  
  - **Qué significa:** Mientras más eventos puede manejar un sistema, más rápido responde. H4 también es cierta.  

---

### Conclusiones  

**`Microservicios:`**  
```
Las empresas grandes los usan más cuando son baratos y rápidos de implementar. Así que, si queremos que más los usen, hay que enfocarse en reducir tiempo y costos.  
```

**`Diseño Basado en Eventos:`** 
``` 
Este diseño hace que los sistemas sean mucho más rápidos y eficientes. Si pueden manejar más eventos por segundo, no solo trabajan mejor, sino que responden más rápido.  
```

---  

