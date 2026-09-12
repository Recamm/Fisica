# Teoría a fondo — Cinemática en una dimensión

Este archivo explica el "por qué" de cada concepto de cinemática. Los ejercicios y el paso a paso resumido ya están en [05-unidad-cinematica.md](05-unidad-cinematica.md); acá está la explicación completa para entenderlo antes de practicar.

## ¿Qué estudia la cinemática?
Estudia el movimiento de los objetos (posición, velocidad, aceleración) sin importar qué fuerzas lo producen (eso lo estudia la dinámica). "En una dimensión" significa que el movimiento ocurre a lo largo de una sola recta (un eje x), no en un plano ni en el espacio.

## Los 3 conceptos básicos
- **Posición (x):** el lugar del eje x donde está el objeto en un instante dado. Siempre se mide respecto de un **sistema de referencia** (un origen que vos elegís). Decir "estoy a 10 m" no significa nada si no aclarás desde dónde.
- **Velocidad (v):** qué tan rápido cambia la posición, y en qué sentido. Si el objeto se mueve en el sentido positivo del eje x, su velocidad es positiva; si se mueve al revés, es negativa. Esto es distinto a como hablamos en la vida diaria (nunca decimos "voy a -20 km/h"), pero en cinemática es fundamental usar el signo correctamente.
- **Aceleración (a):** qué tan rápido cambia la velocidad. Si la velocidad aumenta en módulo, hay aceleración en el mismo sentido que la velocidad; si disminuye, la aceleración va en sentido contrario.

## Espacio recorrido vs. posición (no son lo mismo)
La posición es "dónde estás". El espacio recorrido (o desplazamiento) es "cuánto te moviste": $\Delta x = x_f - x_0$. Podés estar en la posición $x=10\ m$ habiendo recorrido un espacio de solo 2 m (si arrancaste en $x=8\ m$).

## MRU — Movimiento Rectilíneo Uniforme
Es el caso más simple: el objeto se mueve en línea recta con **velocidad constante** (no acelera, $a=0$). Recorre espacios iguales en tiempos iguales.

**Ecuación horaria (la única que realmente se usa para resolver problemas):**
$$x = x_0 + v\cdot t$$

Es la ecuación de una recta si graficás $x$ en función de $t$: la pendiente de esa recta es justamente la velocidad. Esto es clave para leer gráficos: **la pendiente del gráfico posición-tiempo es la velocidad**.

Aunque el MRU casi no aparece solo como ejercicio de examen, es la base de TODO lo demás: los problemas de tiro oblicuo, por ejemplo, tienen un eje que se mueve con MRU.

### Velocidad media
Cuando un objeto no va siempre a la misma velocidad, se define la velocidad media como si hubiera ido a velocidad constante y recorrido la misma distancia en el mismo tiempo total:
$$v_{media} = \frac{\text{espacio total recorrido}}{\text{tiempo total empleado}}$$
**Ojo:** la velocidad media NO es el promedio aritmético de las velocidades de cada tramo (salvo que los tiempos de cada tramo sean iguales). Hay que calcularla siempre con distancia total sobre tiempo total.

## MRUV — Movimiento Rectilíneo Uniformemente Variado
Ahora la velocidad cambia de manera constante (la aceleración es constante, distinta de cero). Las ecuaciones horarias son:
$$x = x_0 + v_0 t + \tfrac{1}{2}at^2 \qquad v_f = v_0 + at$$
Y una tercera ecuación, muy útil cuando no conocés el tiempo:
$$v_f^2 - v_0^2 = 2a(x-x_0)$$

**¿De dónde sale la ecuación complementaria?** Es una combinación algebraica de las dos anteriores (despejando el tiempo de una y reemplazando en la otra), pensada para los casos en que el problema no te da ni te pide el tiempo directamente.

### Lectura de gráficos en MRUV
- En el gráfico posición-tiempo, la curva es una parábola (porque $x$ depende de $t^2$).
- En el gráfico velocidad-tiempo, la pendiente es la aceleración, y el **área bajo la curva** es el espacio recorrido (esto es muy útil para resolver problemas gráficamente sin usar fórmulas).

## Caída libre y tiro vertical (el caso de MRUV que más aparece en el parcial)
Son casos particulares de MRUV donde la aceleración es la de la gravedad, $g = 9{,}80\ m/s^2$. La clave es definir bien el signo:
1. Elegís un sistema de referencia para el eje vertical (puede apuntar hacia arriba o hacia abajo, como prefieras).
2. Si el eje apunta hacia arriba, la aceleración de la gravedad es negativa ($a=-g$), porque siempre apunta hacia abajo.
3. Si el eje apunta hacia abajo, la gravedad es positiva ($a=+g$).
4. Aplicás las mismas ecuaciones de MRUV, con ese signo.

**Caída libre desde el reposo** (el objeto se suelta, no se tira): $v_0 = 0$, entonces
$$h = \tfrac12 g t^2 \qquad v_f = g\cdot t$$

**Tiro vertical hacia arriba:** el objeto sube, frena por la gravedad, llega a $v=0$ en el punto más alto, y luego cae. El tiempo que tarda en subir es igual al tiempo que tarda en volver a la misma altura de la que partió (por simetría del movimiento).

## Problemas de encuentro
Dos cosas "se encuentran" cuando están en la **misma posición** en el **mismo instante** (no alcanza con pasar por el mismo lugar en momentos distintos). El método para resolver siempre es igual:
1. Dibujar la situación y elegir un sistema de referencia común para ambos móviles.
2. Escribir la ecuación horaria de cada uno ($x_A(t)$ y $x_B(t)$), con su signo de velocidad correspondiente.
3. Plantear la condición de encuentro: $x_A = x_B$ para el mismo tiempo $t_e$.
4. Igualar ambas ecuaciones y despejar $t_e$.
5. Reemplazar $t_e$ en cualquiera de las dos ecuaciones para hallar la posición de encuentro.

Esto funciona sin importar si ambos móviles van con MRU, MRUV, si van en el mismo sentido o en sentidos contrarios: el planteo siempre es el mismo.

## Cómo encarar cualquier problema de cinemática 1D, paso a paso
1. Dibujar la situación y elegir un sistema de referencia (origen y sentido positivo).
2. Identificar si es MRU, MRUV, caída libre/tiro vertical, o un problema de encuentro.
3. Escribir la(s) ecuación(es) horaria(s) correspondientes, con los datos y signos correctos.
4. Despejar la incógnita que se pide.
5. Si el problema tiene dos tramos distintos (por ejemplo, caída libre + velocidad constante), resolver cada tramo por separado y después combinar los resultados (sumar tiempos, restar distancias, etc.).

## Por qué este tema es predecible en el parcial
Porque los problemas de cinemática 1D que toman siempre encajan en 4 patrones muy reconocibles (ver [05-unidad-cinematica.md](05-unidad-cinematica.md)): caída libre simple, caída libre con datos de altura, caída libre + tramo a velocidad constante, y problemas de encuentro a velocidad constante. Si entendés bien el "por qué" de cada fórmula acá arriba, vas a poder reconocer el patrón enseguida y aplicar el método correcto sin dudar.
