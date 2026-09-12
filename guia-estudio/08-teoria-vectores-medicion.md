# Teoría a fondo — Medición y Vectores

Este archivo explica los conceptos desde cero, con el "por qué" de cada cosa. Los ejercicios y tips ya los tenés en [02-unidad-vectores-medicion.md](02-unidad-vectores-medicion.md); acá está la explicación completa para entender antes de practicar.

---

## Parte A — Medición

### ¿Para qué sirve todo esto?
En física, cuando medís algo (una longitud, un tiempo, una masa) siempre hay un límite de precisión: nadie puede medir con infinitos decimales. Las reglas de "cifras significativas" existen para que, al hacer cuentas con esos números medidos, el resultado no aparente tener más precisión de la que realmente tenés.

### Cifras significativas: ¿qué cuenta y qué no?
Una cifra significativa es cada dígito que aporta información real sobre la precisión de la medida.
- Todos los dígitos distintos de cero **siempre** cuentan. Ej: `214` tiene 3 cifras significativas.
- Los ceros **entre** dos cifras distintas de cero cuentan. Ej: `7,03` tiene 3 (el 0 del medio cuenta).
- Los ceros a la **izquierda** del primer dígito distinto de cero **no** cuentan, son solo para ubicar la coma. Ej: `0,03` tiene 1 sola cifra significativa (el 3).
- Los ceros a la **derecha**, si hay una coma decimal, sí cuentan. Ej: `81,60` tiene 4 cifras significativas (el último 0 te dice que se midió con esa precisión).

**¿Por qué importa esto?** Porque si decís que algo mide "81,60 cm", estás afirmando que sabés esa medida hasta el centésimo de centímetro. Si en realidad solo mediste "81,6 cm" (3 cifras), agregar un cero de más sería mentir sobre tu precisión.

### Notación científica
Es una forma de escribir números muy grandes o muy chicos como $a \times 10^n$, donde $a$ tiene un solo dígito antes de la coma (entre 1 y 10).
- Para pasar un número a notación científica: contás cuántos lugares te movés la coma hasta que quede un solo dígito antes de ella. Ese número de lugares es el exponente $n$.
  - Ej: `328,65` → mové la coma 2 lugares a la izquierda → `3,2865 × 10²`.
  - Ej: `0,0068` → mové la coma 3 lugares a la derecha → `6,8 × 10⁻³` (exponente negativo porque el número es menor a 1).

### Reglas para operar manteniendo la precisión correcta
- **Sumar o restar:** el resultado se redondea a la cantidad de decimales del término *menos preciso* (el que tiene menos decimales).
  - Ejemplo: $1{,}80\ m + 1{,}425\ m + 0{,}534\ m = 3{,}759\ m$. Como `1,80` solo tiene 2 decimales, el resultado se redondea a 2 decimales: **3,76 m**.
- **Multiplicar o dividir:** el resultado tiene la misma cantidad de cifras significativas que el factor con *menos* cifras significativas.
  - Ejemplo: $2{,}079 \times 10^2 \times 0{,}082 \times 10^{-1}$. El segundo factor tiene solo 2 cifras significativas, entonces el resultado final también se redondea a 2 cifras significativas.

### Análisis dimensional (chequeo rápido de si una fórmula tiene sentido)
Cada magnitud física tiene una "dimensión": longitud (L), masa (M), tiempo (T). Un volumen siempre tiene que dar en unidades de $[L]^3$ (metros cúbicos, por ejemplo). Si te proponen una fórmula como $Vol = \pi r^3 h$, fijate qué dimensión da: $r^3$ ya es $[L]^3$, y multiplicado por $h$ (que es $[L]$) da $[L]^4$ — esto NO puede ser un volumen, así que la fórmula está mal. Este truco te sirve para detectar errores sin necesidad de memorizar todas las fórmulas de memoria.

---

## Parte B — Vectores

### ¿Qué es un vector y por qué no alcanza con un número?
Hay magnitudes que quedan completamente definidas con un solo número (un "escalar"): la temperatura, la masa, el tiempo. Pero hay otras que necesitan además una **dirección** y un **sentido** para tener sentido físico: si te digo "una fuerza de 10 N" no es suficiente información — necesito saber hacia dónde apunta esa fuerza. Eso es un **vector**: una magnitud con módulo (tamaño), dirección (la recta sobre la que actúa) y sentido (hacia qué lado de esa recta apunta).

Ejemplos de magnitudes vectoriales: fuerza, velocidad, aceleración, desplazamiento.
Ejemplos de magnitudes escalares: masa, tiempo, temperatura, densidad, energía.

### Representación gráfica
Un vector se dibuja como una flecha: la longitud de la flecha representa el módulo (a mayor módulo, flecha más larga), y la flecha apunta en la dirección y sentido del vector.

### Componentes de un vector (la herramienta que más vas a usar)
Cualquier vector se puede "descomponer" en dos partes: cuánto vale en la dirección horizontal (x) y cuánto vale en la dirección vertical (y). Es como preguntarse: "¿cuál es la sombra de este vector sobre el eje x? ¿Y sobre el eje y?"

Si conocés el módulo $A$ del vector y el ángulo $\theta$ que forma con el eje x:
$$A_x = A\cos\theta \qquad A_y = A\sin\theta$$

**¿Por qué coseno para x y seno para y?** Porque si dibujás el triángulo rectángulo que forma el vector con sus proyecciones sobre los ejes, el eje x queda como el cateto **adyacente** al ángulo, y el coseno se define justamente como adyacente/hipotenusa. El eje y es el cateto **opuesto**, y el seno es opuesto/hipotenusa.

Para volver de las componentes al módulo, usás el teorema de Pitágoras (porque las componentes forman un triángulo rectángulo con el vector original):
$$A = \sqrt{A_x^2 + A_y^2}$$

Y para encontrar el ángulo que forma con el eje x, usás la tangente ($\tan\theta = A_y/A_x$) y despejás con arcotangente. **Ojo con el cuadrante**: la calculadora te va a dar siempre un ángulo entre -90° y 90°, así que tenés que fijarte en qué cuadrante están realmente $A_x$ y $A_y$ (si ambos son negativos, por ejemplo, el vector apunta al tercer cuadrante y hay que sumarle 180° al resultado de la calculadora).

### Suma y resta de vectores
La regla de oro: **los vectores se suman componente a componente**, no como números sueltos.
$$\vec{A}+\vec{B} = (A_x+B_x,\ A_y+B_y)$$
$$\vec{A}-\vec{B} = (A_x-B_x,\ A_y-B_y)$$

Gráficamente, para sumar dos vectores se usa la "regla del paralelogramo": ponés los dos vectores con su origen en el mismo punto y trazás el paralelogramo que forman; la diagonal de ese paralelogramo es la suma.

### Vectores unitarios ($\hat{i}$, $\hat{j}$, $\hat{k}$)
Son vectores de módulo 1 que apuntan exactamente en la dirección de cada eje: $\hat{i}$ en x, $\hat{j}$ en y, $\hat{k}$ en z. Sirven como "etiquetas": en vez de escribir un vector como $(A_x, A_y)$, lo podés escribir como $A_x\hat{i} + A_y\hat{j}$ — es exactamente lo mismo, solo cambia la notación.

### Producto escalar (el resultado es un número)
$$\vec{A}\cdot\vec{B} = A_xB_x + A_yB_y = |\vec{A}||\vec{B}|\cos\theta$$
Este producto te dice "cuánto de un vector apunta en la dirección del otro". Si los vectores son perpendiculares, el producto escalar da cero (ninguno apunta en la dirección del otro). Si apuntan exactamente igual, da el producto de sus módulos. Se usa mucho para calcular el ángulo entre dos vectores: despejando de la fórmula,
$$\theta = \arccos\left(\frac{\vec{A}\cdot\vec{B}}{|\vec{A}||\vec{B}|}\right)$$

### Producto vectorial (el resultado es OTRO VECTOR)
$$|\vec{A}\times\vec{B}| = |\vec{A}||\vec{B}|\sin\theta$$
A diferencia del producto escalar, este producto da como resultado un vector nuevo, que es **perpendicular al plano formado por A y B**. Para saber hacia qué lado apunta (adelante o atrás del plano, es decir $+\hat{k}$ o $-\hat{k}$), se usa la "regla de la mano derecha": apuntás los dedos en la dirección del primer vector y los "curvás" hacia el segundo vector; el pulgar te indica el sentido del resultado.

En el plano xy, la fórmula práctica para calcular el producto vectorial en componentes es:
$$\vec{A}\times\vec{B} = (A_xB_y - A_yB_x)\hat{k}$$
Si el número que te queda es positivo, el vector resultado apunta "hacia vos" ($+\hat{k}$, saliendo de la hoja). Si es negativo, apunta "hacia adentro de la hoja" ($-\hat{k}$).

### ¿Por qué esto es tan importante para el parcial?
Porque prácticamente todos los ejercicios de estática (fuerzas) e hidrostática usan vectores para representar fuerzas, y el examen SIEMPRE tiene un ejercicio dedicado exclusivamente a operaciones con vectores. Si dominás bien "descomponer, sumar/restar por componentes, sacar módulo y ángulo", ya tenés resuelto ese ejercicio y buena parte de la lógica de estática.
