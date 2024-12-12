
---

#### ¿Qué es CQRS?
CQRS significa **Command Query Responsibility Segregation** o, en español, *Segregación de Responsabilidades de Comandos y Consultas*. Es una forma de organizar cómo se manejan los datos en una aplicación. Básicamente, separa las operaciones que cambian datos (comandos) de las que solo leen datos (consultas). Esto puede hacer que los sistemas sean más rápidos y fáciles de escalar, pero también puede añadir algo de complejidad al implementarlo.

---

#### **Hipótesis**
1. **H1**: Una mejor escalabilidad está relacionada con una menor complejidad en la implementación.
2. **H2**: La reducción de latencia crece a medida que aumenta la adopción global de CQRS.

---

#### **Resultados de los Datos**

**Gráfica 1: Relación entre Escalabilidad y Complejidad**
- A medida que la **escalabilidad mejorada** aumenta, la **complejidad de implementación** tiende a bajar.
- Esto respalda la hipótesis H1: cuanto más se enfoca en mejorar la escalabilidad, menos complicado se vuelve implementar CQRS.

**Gráfica 2: Relación entre Reducción de Latencia y Adopción Global**
- Observamos que cuando la **adopción global** de CQRS crece, la **reducción de latencia** mejora considerablemente.
- Esto valida la hipótesis H2, ya que más adopción parece traducirse en sistemas más rápidos.

**Gráfica 3: Escalabilidad vs. Adopción Global**
- Se nota una tendencia lineal donde, a mayor **adopción global**, mayor es la **escalabilidad** del sistema.

---

#### **Conclusión**
CQRS es una técnica poderosa para manejar datos de manera eficiente en sistemas complejos. Los datos muestran que centrarse en la escalabilidad y la adopción global puede reducir tanto la latencia como la complejidad de implementación.


---