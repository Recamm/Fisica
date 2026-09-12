# Unidad: Cinemática en una dimensión

Siempre es el ejercicio 1 de todas las variantes del parcial (2 puntos), con 4 patrones que se repiten.

## Los 4 patrones que aparecen en los parciales

### Patrón A: caída libre simple (dado el tiempo, pedir altura y/o rapidez)
$$h = \tfrac{1}{2}g t^2 \qquad v_f = g\cdot t$$
*Ejemplo real:* bala que tarda 3,37 s en caer → $h=55,6\ m$, $v_f=33,0\ m/s$.

### Patrón B: caída libre simple (dada la altura, pedir rapidez final)
$$v_f = \sqrt{2gh}$$
*Ejemplo real:* granizo formado a 3000 m → $v_f = 242\ m/s$.

### Patrón C: caída libre + tramo a velocidad constante (paracaidista)
1. Calcular la distancia recorrida en caída libre durante el tiempo dado: $d_1 = \tfrac{1}{2}gt_1^2$.
2. Restar de la altura total para saber a qué altura se abre el paracaídas.
3. Con la distancia restante y la velocidad constante del segundo tramo, calcular el tiempo: $t_2 = d_2/v$.
4. Tiempo total = $t_1+t_2$.
*Ejemplo real:* salto de 300 m, 6,00 s en caída libre, luego 7,50 km/h constante → abre a 124 m, tiempo total 65,3 s.

### Patrón D: encuentro a velocidad constante (tortuga y liebre)
1. Calcular el tiempo que tiene el más lento para llegar a la meta: $t = d_{lento}/v_{lento}$.
2. Con ese mismo tiempo, calcular la velocidad que necesita el otro para recorrer su distancia: $v_{rápido} = d_{rápido}/t$.
*Ejemplo real:* tortuga a 0,250 m/s a 4,50 m de la meta, liebre a 204,5 m → liebre necesita 40,9 km/h.

## Fórmulas de respaldo (por si el problema no encaja en los 4 patrones)
- MRUV general: $x = x_0 + v_0t + \tfrac12at^2$; $v_f=v_0+at$; $v_f^2-v_0^2=2a(x-x_0)$.
- Tiro vertical hacia arriba: mismas fórmulas con $a=-g$ si "arriba" es positivo. En el punto más alto, $v=0$.
- Gráficos: pendiente de x-t = velocidad; pendiente de v-t = aceleración; área bajo v-t = desplazamiento.

## Ejercicios de práctica adicionales (de `Semana 5/Actividades`, para entrenar variantes)
- Antílope con aceleración constante que recorre 70,0 m en 7,00 s, llegando al segundo punto a 15,0 m/s → hallar rapidez inicial y aceleración (usar las 2 ecuaciones de MRUV con incógnitas $v_0$ y $a$).
- Cohete que acelera y luego sigue con velocidad inicial ganada en tiro vertical (combinar tramo con aceleración + tramo de caída libre).
- Comparación de gravedad en otro planeta a partir del tiempo de caída (despejar $g$ de $h=\tfrac12 g t^2$, con la misma altura en ambos casos).

## Errores comunes a evitar
- No definir el signo de $g$ según el sistema de referencia elegido (arriba positivo o abajo positivo) — mezclar signos es el error #1.
- En problemas de "cae y después va a velocidad constante", olvidar que la velocidad al final de la caída libre NO se usa después (el segundo tramo es a velocidad constante impuesta, no la que trae).
- En problemas de encuentro, no verificar que ambos móviles usan el **mismo tiempo** de referencia.
