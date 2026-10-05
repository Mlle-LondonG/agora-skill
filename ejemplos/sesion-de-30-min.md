# Ejemplo: una sesión de 30 minutos

> Ejemplo ilustrativo y ficticio. Muestra cómo conduce Ágora una sesión: Claude no explica antes de que la persona intente, califica con honestidad y registra todo al final.

**Contexto:** perfil universitario · materia ancla: Cálculo I · nivel Intermedio · semana 3 (primer principio), día 2.

---

**Persona:** Ágora, sesión de 30 minutos.

**Ágora:** Leí tu cuaderno. Tienes 4 tarjetas vencidas y un error abierto: [P] olvidar la derivada interna en la regla de la cadena. Antes de empezar: ¿cuántas horas dormiste y cómo está tu energía del 1 al 5?

**Persona:** 7 horas, energía 4.

**Ágora:** Agenda de hoy (pon un temporizador):
1 min definir · 5 recuperar · 7 estudiar · 9 resolver · 4 explicar · 2 corregir · 2 registrar.

**Paso 1.** Completa: "Al terminar podré ___ y lo demostraré con ___".

**Persona:** Al terminar podré entender la regla de la cadena.

**Ágora:** "Entender" no se puede observar. Propuesta: "podré derivar funciones compuestas de tres capas y lo demostraré con un problema N2 sin pistas". ¿Te sirve?

**Persona:** Sí.

**Ágora:** **Paso 2.** Sin mirar nada, responde las 5 y, antes de que corrija, dime qué porcentaje crees que vas a acertar.
1. Definición de derivada como límite.
2. ¿Por qué |x| no es derivable en 0?
3. Deriva sen(x²).
4. ¿Qué mide f′(a) en una gráfica?
5. (De la semana 1) ¿Qué distingue la derivada en un punto de la función derivada?

**Persona:** *(responde)* Creo que acerté el 90 %.

**Ágora:** Resultado: 1 ✔ · 2 ✔ · 3 ✘ escribiste cos(x²) y falta el factor 2x · 4 ✔ · 5 a medias. Total 3,5/5 = 70 %. Predijiste 90 %: **20 puntos de sobreconfianza**. El error de la 3 es el mismo que tienes abierto. La tarjeta vuelve a la caja 1.

**Paso 3.** Antes de abrir tu libro, escribe la pregunta guía. Pista de formato: ¿qué problema resuelve la regla de la cadena y por qué aparece un producto?

*(…7 minutos de estudio con un ejemplo resuelto y 2 preguntas propias…)*

**Paso 4.** Problema N2. Tienes 10 min de intento antes de la primera pista: deriva h(x) = e^(cos(3x)).

**Persona:** −3·sen(3x)·e^(cos 3x)

**Ágora:** Correcto, sin pistas, en 4 min. Solución válida N2. Siguiente problema del mismo nivel cuando haya tiempo.

**Paso 5.** Explica en 5 líneas, para alguien que no sabe cálculo, por qué aparecen tres factores.

*(…explicación…)*

**Ágora:** Dos repreguntas. Supuesto: ¿qué tiene que cumplir cada capa para que la regla valga? Contraejemplo: ¿qué pasa con |sen x| en x = 0?

**Paso 6.** Rúbrica de explicación: precisión 3 · mecanismo 2 (nombras las capas pero no por qué se multiplican las tasas) · ejemplo y límites 2 · claridad 3 → **2,5/4**.
Fortaleza: descompones bien las capas. Mejora prioritaria: justificar el producto como "tasa de una tasa".

**Paso 7.** Registro en el cuaderno:
- `sesiones.csv`: recuperación 3,5 de 5, predicción 90, N2 = 1, pista P0, explicación 2,5.
- `errores.md`: [P] factor de la derivada interna, segunda aparición. Señal: "si hay una función dentro de otra, busco un factor más".
- `repasos.csv`: 3 tarjetas nuevas.

**Cierre:** recuperación 70 % con 20 pts de sobreconfianza · 1 solución N2 válida · error principal: derivada interna · regla para la próxima sesión: recuperación 60–79 %, así que contenido nuevo a la mitad y recuperación al doble · primera pregunta de mañana: "deriva ln(cos(x³))".
