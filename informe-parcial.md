# Informe del Primer Parcial — Física (Cátedra Torti)

## 1. Idea general: por qué "son siempre los mismos 4 ejercicios"

Analizando los 8 temas del parcial del 07/05/2026 (todos son el mismo examen con distintos números, para evitar copia entre compañeros de al lado) se ve un patrón clarísimo: **el parcial tiene siempre 4 ejercicios**, cada uno de un tema distinto, y **la estructura interna de cada ejercicio es idéntica entre temas**. Lo único que cambia de un "Tema" a otro son:

- Los valores numéricos (masas, ángulos, densidades, distancias, tiempos).
- A veces se pide el mismo dato con otra "cara" (ej: en vez de A+B piden A−B; en vez de calcular con qué % del volumen flota, piden la fuerza normal en el fondo).
- El objeto de la consigna (esfera de aluminio → esfera de magnesio; persona de 75 kg → persona de 95 kg), pero el modelo físico y el método de resolución son exactamente el mismo.

Los 4 ejercicios, en el orden en que suelen aparecer, son:

| # | Tema | Qué evalúa | Peso aprox. |
|---|------|-----------|-------------|
| 1 | **Estática** (equilibrio de cuerpo rígido) | Sumatoria de fuerzas y de momentos = 0 | 2 puntos |
| 2 | **Cinemática en una dimensión** (caída libre / MRUV) | Ecuaciones de movimiento con aceleración constante | 2 puntos |
| 3 | **Hidrostática** (empuje, densidad, presión) | Arquímedes + equilibrio de fuerzas sobre un cuerpo sumergido o flotando | 4 puntos (el que más vale) |
| 4 | **Vectores** (suma/resta y producto vectorial) | Descomposición en componentes, módulo, ángulo, producto vectorial | 2 puntos |

Total: 10 puntos. Si entendés **la lógica** de cada uno de estos 4 (no la memorización de un ejercicio puntual), podés resolver cualquier variante que te tomen, porque el procedimiento no cambia — solo los números que reemplazás en las mismas fórmulas.

Datos que la cátedra fija siempre igual (no cambian entre temas):
- $g = 9{,}80\ m/s^2$ (te lo dan en el enunciado, pero siempre es este valor).
- Los resultados se expresan con **3 cifras significativas y unidades**. Perder esta regla resta puntos aunque la cuenta esté bien.
- Casi siempre piden también el **diagrama de cuerpo libre (DCL)** en el ejercicio de hidrostática.

---

## 2. Ejercicio tipo 1 — Estática (equilibrio de una tabla/palanca)

### Cómo se plantea siempre
Una tabla (o barra) homogénea, apoyada/basculando sobre un punto de apoyo (llamado "a" en el enunciado), con:
- Una persona parada en un extremo (su peso actúa como fuerza puntual en ese extremo).
- Una cuerda atada en el otro extremo, formando un ángulo con la vertical (o la horizontal, según el tema).
- Te dan: masa de la persona, masa de la tabla, longitud de la tabla, dónde está el punto de apoyo, y el ángulo de la cuerda.
- Te piden: la tensión de la cuerda.

Las variantes (grúa levantando un auto, dos carros con poleas, dos personas pescando) son la misma idea: **un sistema en equilibrio estático**, donde tenés que decidir si alcanza con sumar fuerzas o si además hay que sumar momentos.

### Justificación física (por qué se resuelve así)
- Un cuerpo en reposo (que no se traslada ni rota) cumple la **primera condición de equilibrio** (ΣF = 0 en x e y) y, si las fuerzas no son concurrentes (no pasan todas por el mismo punto, como en una tabla que puede girar), también la **segunda condición de equilibrio** (ΣM = 0, suma de momentos/torques nula).
- El **momento de una fuerza** respecto de un punto O es $M_O = F \cdot d$, con $d$ la distancia perpendicular entre la recta de acción de la fuerza y el punto O (brazo de palanca).
- **Truco clave**: si tomás el punto de apoyo/articulación como centro de momentos, la fuerza que actúa ahí (normal, reacción del pivote) tiene brazo = 0 y desaparece de la ecuación. Así te queda una sola incógnita (la tensión) en una sola ecuación.

### Resolución paso a paso (ejemplo real, Tema 1)

**Enunciado**: Persona de 75,0 kg parada en el extremo de una tabla homogénea (20,0 kg, 3,00 m), que bascula en un punto "a" ubicado a 1,00 m del extremo izquierdo. La cuerda en el extremo izquierdo forma 20,0° con la vertical. Calcular la tensión.

**Paso 1 — Identificar el sistema y armar el DCL.**
La tabla tiene 3 fuerzas relevantes que generan momento respecto del punto de apoyo "a":
- El peso de la persona, aplicado en el extremo derecho (a 2,00 m de "a", porque la tabla mide 3,00 m y "a" está a 1,00 m del extremo izquierdo → 3,00 − 1,00 = 2,00 m).
- El peso de la tabla, aplicado en su centro geométrico (a 1,50 m del extremo izquierdo, es decir a 0,50 m de "a", porque 1,50 − 1,00 = 0,50 m).
- La tensión de la cuerda, aplicada en el extremo izquierdo (a 1,00 m de "a"), formando 20,0° con la vertical. Solo la componente perpendicular a la tabla genera momento; como la tabla es horizontal, esa componente perpendicular es $T\cos(20°)$ (la componente horizontal de T no genera momento porque su brazo respecto de la tabla horizontal es nulo... en la práctica, se usa el ángulo con la vertical directamente: el brazo efectivo es el brazo geométrico × cos(ángulo con la vertical)).

**Paso 2 — Elegir sentido positivo y plantear ΣM = 0 en el punto "a".**
El peso de la persona y el peso de la tabla giran la tabla en sentido antihorario (bajan el extremo derecho); la tensión la gira en sentido horario (sube el extremo izquierdo). Igualando ambos sentidos:

$$P_{persona}\cdot d_{persona} + P_{tabla}\cdot d_{tabla} = T\cos(20°)\cdot d_{cuerda}$$

$$75{,}0\ kg \cdot 9{,}80\ \tfrac{m}{s^2} \cdot 2{,}00\ m + 20{,}0\ kg \cdot 9{,}80\ \tfrac{m}{s^2} \cdot 0{,}50\ m - T\cos(20°)\cdot 1{,}00\ m = 0$$

**Paso 3 — Despejar T.**
$$T = \frac{75{,}0 \cdot 9{,}80 \cdot 2{,}00 + 20{,}0 \cdot 9{,}80 \cdot 0{,}50}{\cos(20°)\cdot 1{,}00} = \frac{1470 + 98{,}0}{0{,}9397}$$

$$T \approx 1{,}67 \times 10^3\ N$$

**Justificación del resultado**: la tensión debe ser mayor que la suma de los pesos "efectivos" porque su brazo de palanca (con el coseno del ángulo) es más corto que el brazo de la persona; para compensar un momento grande con un brazo relativamente chico, la fuerza tiene que ser grande.

### Cómo identificar variantes de este ejercicio
- Si en vez de una persona y una tabla te dan una grúa y un auto, o dos carros con poleas: el método es igual, cambia el dibujo, pero seguís poniendo ΣF = 0 y/o ΣM = 0.
- Si hay más de un cuerpo (ej. dos carros unidos por una cuerda), primero analizás cada cuerpo por separado (DCL individual) y después heredás la tensión común entre ambos como incógnita compartida.
- Presta atención a si el ángulo dado es respecto de la **vertical** o de la **horizontal**: eso decide si usás seno o coseno en la componente que necesitás.

---

## 3. Ejercicio tipo 2 — Cinemática en una dimensión (caída libre / MRUV)

### Cómo se plantea siempre
Un objeto que cae (o sube y luego cae, o se mueve a velocidad constante en un tramo y con aceleración en otro). Te dan un dato (tiempo de caída, altura inicial, velocidad de descenso constante) y te piden otro (altura, rapidez final, tiempo total).

Variantes típicas:
- Caída libre simple desde el reposo (dan tiempo, piden altura y velocidad final).
- Caída con rozamiento donde se alcanza una velocidad límite/constante (el "granizo").
- Problema mixto: caída libre + tramo a velocidad constante (paracaidista).
- Problema de encuentro entre dos móviles (tortuga y liebre).

### Justificación física
Todos son casos de **Movimiento Rectilíneo Uniformemente Variado (MRUV)**, con $a = \pm g$ cuando hay caída libre, o de **Movimiento Rectilíneo Uniforme (MRU)** cuando la velocidad es constante. Las ecuaciones fundamentales son:

$$x = x_0 + v_0 t + \tfrac{1}{2}at^2 \qquad v_f = v_0 + at \qquad v_f^2 - v_0^2 = 2a(x - x_0)$$

Para caída libre desde el reposo ($v_0 = 0$): $h = \tfrac{1}{2}gt^2$ y $v_f = g\cdot t$.

### Resolución paso a paso (ejemplo real, Tema 1)

**Enunciado**: Se suelta un objeto (parte del reposo) y tarda 3,37 s en llegar al suelo. Calcular a) la altura desde la que cayó, b) la rapidez al llegar al suelo.

**Paso 1 — Identificar el tipo de movimiento y las condiciones iniciales.**
"Se deja caer" ⇒ $v_0 = 0$. Es caída libre, por lo tanto $a = g = 9{,}80\ m/s^2$ (tomando como positivo el sentido de caída).

**Paso 2 — Aplicar la ecuación de posición para hallar la altura.**
$$h = \tfrac{1}{2}g t^2 = \tfrac{1}{2}\cdot 9{,}80\ \tfrac{m}{s^2}\cdot(3{,}37\ s)^2 = 55{,}6\ m$$

**Paso 3 — Aplicar la ecuación de velocidad para hallar la rapidez final.**
$$v_f = g\cdot t = 9{,}80\ \tfrac{m}{s^2}\cdot 3{,}37\ s = 33{,}0\ m/s$$

**Justificación**: no hace falta usar $v_f^2 = v_0^2 + 2gh$ porque ya tenemos el tiempo directamente; se usan las ecuaciones que relacionan las variables que el enunciado da y pide, evitando pasos innecesarios.

### Cómo identificar variantes
- Si te dan una velocidad final constante después de la caída libre (paracaidista): primero resolvés la caída libre normal (para saber cuánto cayó y a qué velocidad llegó a rapidez terminal — dato que no se usa después), y luego con la altura restante y la velocidad constante usás $x = v \cdot t$ (MRU) para el segundo tramo.
- Si te dan una altura inicial (ej. "se forma a 2000 m") y piden la rapidez de llegada, usás $v_f^2 = 2gh$ (sale de $v_f^2 - v_0^2 = 2a\Delta x$ con $v_0=0$).
- Problemas de encuentro (tortuga/liebre): planteás la posición de cada uno en función del tiempo, $x_A(t) = x_B(t)$, y despejás el tiempo o la velocidad pedida.

---

## 4. Ejercicio tipo 3 — Hidrostática (empuje y equilibrio de un cuerpo en un fluido)

### Cómo se plantea siempre
Una esfera (o cubo, o estatua) maciza de un material dado (te dan diámetro/arista y densidad), sumergida en un líquido (te dan su densidad). Puede estar:
- **Apoyada en el fondo** (más densa que el líquido → se hunde y necesita normal).
- **Flotando** (menos densa que el líquido → emerge una fracción del volumen).
- **Colgando de una cuerda, sumergida** (tensión = peso aparente).

Te piden: masa (a partir del volumen y la densidad), fuerza de empuje, fuerza normal (o tensión, o % de volumen sumergido/emergido), y casi siempre el diagrama de cuerpo libre.

### Justificación física
- **Densidad**: $\delta = m/V \Rightarrow m = \delta \cdot V$.
- **Empuje (Arquímedes)**: $E = \delta_{líquido}\cdot V_{sumergido}\cdot g$. Físicamente es el peso del volumen de líquido que el cuerpo desaloja.
- El cuerpo está en equilibrio (no se mueve), entonces ΣF = 0. Según el caso:
  - Apoyado en el fondo: $E + N - P = 0 \Rightarrow N = P - E$ (si diera negativo, el cuerpo en realidad flotaría, no necesitaría normal).
  - Flotando libremente: $E = P \Rightarrow \delta_{líquido}\cdot V_{sumergido}\cdot g = \delta_{cuerpo}\cdot V_{total}\cdot g \Rightarrow \dfrac{V_{sumergido}}{V_{total}} = \dfrac{\delta_{cuerpo}}{\delta_{líquido}}$.
  - Colgado de una cuerda, sumergido: $T + E - P = 0 \Rightarrow T = P - E$.

### Resolución paso a paso (ejemplo real, Tema 1)

**Enunciado**: Esfera maciza de aluminio ($\delta = 2{,}70\times10^3\ kg/m^3$) de 3,00 cm de diámetro, apoyada en el fondo de un recipiente con alcohol ($\delta = 7{,}89\times10^2\ kg/m^3$). Calcular a) masa en gramos, b) fuerza de empuje, c) fuerza normal en el fondo, d) DCL.

**Paso 1 — Calcular el volumen de la esfera a partir del diámetro.**
Radio = diámetro/2 = 1,50 cm = 0,0150 m.
$$V = \tfrac{4}{3}\pi r^3 = \tfrac{4}{3}\pi (0{,}0150\ m)^3 = 1{,}4137\times10^{-5}\ m^3$$

**Paso 2 — Calcular la masa con la densidad del material de la esfera.**
$$m = \delta_{esfera}\cdot V = 2{,}70\times10^3\ \tfrac{kg}{m^3}\cdot 1{,}4137\times10^{-5}\ m^3 = 0{,}03817\ kg = 38{,}2\ g$$

**Paso 3 — Calcular el empuje con la densidad del líquido (no la del material de la esfera).**
Como la esfera está totalmente sumergida, el volumen desalojado es todo el volumen de la esfera:
$$E = \delta_{líquido}\cdot V\cdot g = 7{,}89\times10^2\ \tfrac{kg}{m^3}\cdot 1{,}4137\times10^{-5}\ m^3\cdot 9{,}80\ \tfrac{m}{s^2} = 0{,}109\ N$$

**Paso 4 — Plantear equilibrio de fuerzas sobre la esfera para hallar la normal.**
Sobre la esfera actúan tres fuerzas: peso (P, hacia abajo), empuje (E, hacia arriba) y normal del fondo (N, hacia arriba). Como está en reposo, ΣF = 0:
$$E + N - P = 0 \Rightarrow N = P - E = m\cdot g - E = 0{,}03817\ kg\cdot9{,}80\ \tfrac{m}{s^2} - 0{,}109\ N = 0{,}265\ N$$

**Paso 5 — DCL**: tres flechas desde el centro de la esfera: P hacia abajo (la más larga, porque es la fuerza dominante), E hacia arriba (chica), N hacia arriba (chica), de modo que E + N (arriba) equilibre a P (abajo).

**Justificación del resultado**: N dio positivo y del mismo orden que P, lo cual es coherente: el aluminio (δ=2700) es mucho más denso que el alcohol (δ=789), entonces el empuje es chico comparado con el peso y hace falta que el fondo sostenga casi todo el peso.

### Cómo identificar variantes
- Si el cuerpo **flota** en vez de apoyarse en el fondo, no hay normal: se usa $E = P$ y se despeja el volumen o fracción sumergida/emergida.
- Si piden "% del volumen que queda sumergido", es directamente $\dfrac{\delta_{cuerpo}}{\delta_{líquido}}\times 100$.
- Si te dan presión a una profundidad, usás $p = p_0 + \delta\cdot g\cdot h$ en vez de la fuerza de empuje directamente.
- Siempre fijate con qué densidad corresponde calcular cada cosa: la masa del cuerpo usa **la densidad del cuerpo**; el empuje usa **la densidad del líquido**. Es el error más común.

---

## 5. Ejercicio tipo 4 — Vectores (suma/resta y producto vectorial)

### Cómo se plantea siempre
Te dan dos vectores A y B (representando fuerzas), cada uno con su módulo y el ángulo que forma con algún eje de referencia (usualmente mostrados en una figura, con ángulos tipo 30°, 35°). Te piden:
- El módulo y el ángulo (respecto de algún eje) de $\vec{A}+\vec{B}$ o de $\vec{A}-\vec{B}$.
- El producto vectorial $\vec{A}\times\vec{B}$ (módulo, dirección y sentido).

### Justificación física
- Para sumar o restar vectores hay que trabajar **componente a componente**, no con los módulos directamente (salvo casos particulares como vectores colineales).
- $A_x = A\cos\theta$, $A_y = A\sin\theta$, donde $\theta$ es el ángulo del vector medido desde el eje +x (si el ángulo dado en el enunciado es respecto de otro eje, hay que convertirlo primero).
- Módulo de la resultante: $|\vec{R}| = \sqrt{R_x^2+R_y^2}$; ángulo: $\theta_R = \arctan(R_y/R_x)$, prestando atención al cuadrante en el que cae el vector resultante.
- Producto vectorial: $|\vec{A}\times\vec{B}| = |\vec{A}||\vec{B}|\sin\theta$, donde $\theta$ es el ángulo **entre** A y B (no el ángulo de cada uno respecto del eje). La dirección es perpendicular al plano (versor $\hat{k}$) y el sentido sale de la regla de la mano derecha.

### Resolución paso a paso (ejemplo real, Tema 1)

**Enunciado**: Vector A de módulo 32,0 N a 30,0° (de un eje de referencia) y vector B de módulo 40,0 N a 35,0° (de otro eje, según la figura). Calcular a) módulo y ángulo de A+B respecto del eje x, b) A×B.

**Paso 1 — Pasar cada vector a componentes x e y**, usando los ángulos tal como están definidos en la figura del enunciado (en este caso, A medido desde el eje x, y B medido desde el eje y, por eso B usa seno para x y coseno para y):
$$A_x = 32{,}0\cos(30{,}0°) \qquad A_y = 32{,}0\sin(30{,}0°)$$
$$B_x = 40{,}0\sin(35{,}0°) \qquad B_y = 40{,}0\cos(35{,}0°)$$

**Paso 2 — Sumar componente a componente.**
$$R_x = A_x + B_x \qquad R_y = A_y + B_y$$

**Paso 3 — Calcular el módulo de la resultante.**
$$|\vec{A}+\vec{B}| = \sqrt{R_x^2+R_y^2} = 70{,}3\ N$$

**Paso 4 — Calcular el ángulo respecto del eje +x**, usando arcotangente y verificando el cuadrante (acá R cae en el primer cuadrante, por lo que el resultado de la arctan ya es el ángulo final sin ajustes):
$$\theta = \arctan\left(\frac{R_y}{R_x}\right) = 43{,}9°$$

**Paso 5 — Calcular el producto vectorial usando el ángulo entre A y B** (no los ángulos de cada uno respecto del eje; hay que restar/sumar los ángulos de la figura para obtener el ángulo entre ambos vectores, en este caso 30° + 35° − ... = 25°, según la geometría de la figura):
$$|\vec{A}\times\vec{B}| = |A||B|\sin(\theta_{entre}) = 32{,}0\cdot 40{,}0\cdot\sin(25°) = 541\ N^2$$

El sentido, por regla de la mano derecha (A hacia B girando en sentido antihorario en el plano), da $+\hat{k}$:
$$\vec{A}\times\vec{B} = 541\ N^2\ \hat{k}$$

**Justificación**: el módulo de la suma (70,3 N) es menor que la suma aritmética de los módulos (32,0+40,0=72,0 N) porque los vectores no son colineales; cuanto más separados estén en ángulo, más "se cancelan" parcialmente entre sí. El producto vectorial depende del **seno** del ángulo entre ellos (no del coseno, que es para el producto escalar), y su resultado es un área con dirección perpendicular al plano de los vectores.

### Cómo identificar variantes
- Si piden $\vec{A}-\vec{B}$ en vez de $\vec{A}+\vec{B}$: mismo procedimiento, pero $R_x = A_x - B_x$, $R_y = A_y - B_y$. El ángulo puede pedirse respecto del eje y en vez del eje x: en ese caso, después de tener el ángulo respecto del eje x, hay que convertirlo (90° − ese ángulo, o ajustar según el cuadrante).
- Prestá mucha atención a **respecto de qué eje está definido cada ángulo en la figura** del enunciado — es la fuente más común de error, no la fórmula en sí.
- Para el producto vectorial, el ángulo que usás es siempre el ángulo entre los dos vectores (súmalos o réstalos según la figura), nunca el ángulo de uno solo respecto del eje.

---

## 6. Resumen de checklist para el día del parcial

1. **Estática**: ¿es un cuerpo rígido con posibilidad de rotar? → ΣF=0 y ΣM=0, elegí el punto de apoyo como centro de momentos para eliminar una incógnita.
2. **Cinemática**: identificá $v_0$, si hay o no aceleración, y qué dato te dan vs. qué te piden, para elegir la ecuación de MRUV que conecte ambos directamente.
3. **Hidrostática**: identificá si el cuerpo está apoyado en el fondo (necesita N), flotando (E=P) o colgado (T=P−E). No confundas la densidad del cuerpo con la del líquido.
4. **Vectores**: pasá todo a componentes con los ángulos tal como los da la figura, sumá/restá componente a componente, y para el producto vectorial usá el ángulo **entre** los vectores, no el de cada uno respecto del eje.
5. Siempre: 3 cifras significativas + unidades, y $g=9{,}80\ m/s^2$.
