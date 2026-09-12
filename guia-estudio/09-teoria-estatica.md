# Teoría a fondo — Estática

Este archivo explica el "por qué" de cada concepto de estática. Los ejercicios y el paso a paso resumido ya están en [03-unidad-estatica.md](03-unidad-estatica.md); acá está la explicación completa para entenderlo antes de practicar.

## ¿Qué problema resuelve la estática?
La estática se usa para calcular fuerzas sobre cuerpos que están quietos (en equilibrio): un cartel colgado, una persona parada sobre una tabla, un auto levantado por una grúa. La pregunta que siempre se responde es: **¿cuánto vale tal o cual fuerza para que el cuerpo se mantenga quieto?** Esto es clave en ingeniería: el grosor de un cable, de una columna o de una viga se calcula sabiendo qué fuerza tiene que soportar.

## ¿Qué es una fuerza?
Es la acción de empujar, tirar o arrastrar algo. Se representa con una flecha (porque es un vector: tiene módulo, dirección y sentido). Las fuerzas más comunes en los problemas:
- **Peso ($P = m \cdot g$):** la Tierra atrae a todo hacia abajo. Siempre apunta hacia abajo, aplicado en el centro de gravedad del cuerpo.
- **Tensión (T):** la fuerza que hace una cuerda o cable al estar estirado, tirando hacia donde apunta la cuerda.
- **Normal (N):** la fuerza de contacto que hace una superficie, siempre perpendicular a esa superficie, "empujando" al cuerpo para que no la atraviese.
- **Empuje (E):** cuando hay un líquido de por medio (esto lo vas a ver en detalle en hidrostática).

## Fuerzas concurrentes vs. no concurrentes
- **Concurrentes (o copuntuales):** todas las fuerzas que actúan sobre el cuerpo pasan por el mismo punto. Ejemplo: un cuadro colgado por dos cuerdas que se juntan arriba del cuadro.
- **No concurrentes:** las fuerzas están aplicadas en distintos puntos del cuerpo. Ejemplo: una tabla apoyada en dos puntos distintos, con un peso en el medio.

Esta distinción es CLAVE porque cambia qué ecuaciones necesitás:
- Si son concurrentes, con que la suma de fuerzas en x sea cero y la suma en y sea cero, alcanza (el cuerpo no se traslada, y como todas pasan por el mismo punto, tampoco puede girar).
- Si NO son concurrentes, puede pasar que la suma de fuerzas dé cero (no hay traslación) pero el cuerpo esté girando igual. Por eso hace falta una tercera ecuación: la de momentos.

## Condición de equilibrio para fuerzas concurrentes
$$\sum F_x = 0 \qquad \sum F_y = 0$$
Esto significa: sumás las componentes en x de todas las fuerzas (con su signo) y tiene que dar cero; lo mismo para y. Método práctico:
1. Descomponer cada fuerza en $F_x = F\cos\theta$ y $F_y = F\sin\theta$.
2. Sumar todas las componentes x, sumar todas las componentes y.
3. Plantear que ambas sumas son cero, y despejar la incógnita.

## Momento de una fuerza (torque) — el concepto más importante de la unidad
Cuando una fuerza no pasa por el punto de apoyo/pivote de un cuerpo, tiende a hacerlo **girar**. La magnitud que mide "cuánto tiende a girar" una fuerza respecto de un punto se llama **momento** (o torque):
$$M_O = F \cdot d$$
donde $d$ es la distancia **perpendicular** entre el punto O y la recta sobre la que actúa la fuerza (esta distancia se llama "brazo de palanca").

**Intuición:** pensá en abrir una puerta. Si empujás justo en el borde (lejos de la bisagra), con poca fuerza la abrís fácil. Si empujás cerca de la bisagra, necesitás mucha más fuerza para el mismo efecto. Eso es porque el momento depende de la distancia al punto de giro (la bisagra): a mayor distancia, mayor momento con la misma fuerza.

**Signo del momento:** una fuerza puede hacer girar un cuerpo en sentido horario o antihorario. Antes de resolver un problema, elegís arbitrariamente cuál sentido considerás positivo (por ejemplo, "antihorario positivo"), y sos consistente con esa elección durante todo el problema.

## Condición de equilibrio para fuerzas no concurrentes
Además de que no haya traslación, hace falta que no haya rotación:
$$\sum F_x = 0 \qquad \sum F_y = 0 \qquad \sum M_O = 0$$

**Truco clave:** elegí el punto O (centro de momentos) en un lugar donde una fuerza desconocida tenga brazo cero (por ejemplo, en un apoyo o articulación). Así esa fuerza desaparece de la ecuación de momentos porque $M = F \cdot 0 = 0$, y podés despejar directamente lo que te falta sin resolver un sistema de 3 ecuaciones con 3 incógnitas.

## Centro de gravedad
Es el punto donde se considera aplicado el peso de un cuerpo. Si el cuerpo es simétrico y homogéneo (como una tabla uniforme), el centro de gravedad coincide con el centro geométrico (el punto medio, si es una barra). Esto es fundamental porque en casi todos los problemas de "tabla que bascula" o "barra apoyada", el peso propio del objeto actúa en su punto medio.

## Cómo encarar cualquier problema de estática, paso a paso
1. **Dibujar el cuerpo aislado** con TODAS las fuerzas que actúan sobre él (diagrama de cuerpo libre).
2. Identificar si las fuerzas son concurrentes o no.
3. Si son concurrentes: plantear $\sum F_x=0$ y $\sum F_y=0$.
4. Si no son concurrentes (hay una barra, tabla, viga extendida): elegir un punto de referencia (idealmente un apoyo) y plantear $\sum M_O=0$, además de las ecuaciones de fuerzas si hacen falta.
5. Resolver las ecuaciones (a veces con una sola ecuación de momentos ya alcanza).

## Por qué este tema pesa tanto en el parcial
Porque además de ser un ejercicio propio (torque, equilibrio de una tabla o una grúa), reaparece combinado con hidrostática cuando hay una palanca con contrapeso y un cuerpo sumergido. Entender bien el concepto de momento es la base para resolver ambos tipos de ejercicios.
