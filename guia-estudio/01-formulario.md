# Formulario único — Física UBA XXI (1er cuatrimestre)

⭐ = aparece en los 8 temas del parcial analizado (altísima frecuencia)

## 0. Medición (base, no es ejercicio propio del parcial)
- Cifras significativas: los ceros a la izquierda no cuentan; los ceros a la derecha del punto decimal sí cuentan.
- Notación científica: $a \times 10^n$ con $1 \le a < 10$.
- Al sumar/restar: el resultado tiene tantos decimales como el término con menos decimales.
- Al multiplicar/dividir: el resultado tiene tantas cifras significativas como el factor con menos cifras.
- Análisis dimensional: verificar que ambos lados de una ecuación tengan las mismas unidades/dimensiones (L, M, T).

## 1. Vectores ⭐
- Componentes: $A_x = A\cos\theta$, $A_y = A\sin\theta$ (θ medido desde el eje x).
- Módulo: $|\vec{A}| = \sqrt{A_x^2 + A_y^2}$.
- Suma/resta: se hace componente a componente. $\vec{A}+\vec{B} = (A_x+B_x, A_y+B_y)$.
- Ángulo del vector resultante: $\theta = \arctan(R_y/R_x)$ (cuidado con el cuadrante).
- Producto escalar: $\vec{A}\cdot\vec{B} = A_xB_x + A_yB_y = |\vec{A}||\vec{B}|\cos\theta$.
- Ángulo entre dos vectores: $\theta = \arccos\left(\dfrac{\vec{A}\cdot\vec{B}}{|\vec{A}||\vec{B}|}\right)$.
- Producto vectorial (módulo): $|\vec{A}\times\vec{B}| = |\vec{A}||\vec{B}|\sin\theta$, dirección con regla de la mano derecha (perpendicular al plano, versor $\hat{k}$).
  - En componentes 2D: $\vec{A}\times\vec{B} = (A_xB_y - A_yB_x)\hat{k}$.
- Vectores unitarios: $\vec{V} = V_x\hat{i} + V_y\hat{j}$.

## 2. Estática ⭐ (equilibrio de cuerpo rígido)
- Fuerzas concurrentes (pasan por el mismo punto): alcanza con
  $$\sum F_x = 0 \qquad \sum F_y = 0$$
- Fuerzas no concurrentes: además hay que anular el momento (torque):
  $$\sum F_x = 0 \qquad \sum F_y = 0 \qquad \sum M_O = 0$$
- Momento de una fuerza respecto de un punto O: $M_O = F \cdot d$, donde $d$ es la distancia perpendicular (brazo de palanca) entre la recta de acción de la fuerza y el punto O.
- Convención: elegir un sentido positivo (horario o antihorario) y ser consistente.
- Truco práctico: tomar momentos respecto de un punto de apoyo/articulación para que su fuerza (normal o reacción) no aparezca en la ecuación (brazo = 0).
- Peso: $P = m \cdot g$.
- Diagrama de cuerpo libre (DCL): siempre dibujar TODAS las fuerzas que actúan sobre el cuerpo aislado (peso, normales, tensiones, empuje si aplica).

## 3. Hidrostática ⭐ (la que más puntaje suele tener)
- Densidad: $\delta = m/V$.
- Presión: $p = F/A$ (unidad SI: Pascal, $1\,Pa = 1\,N/m^2$).
- Presión a una profundidad $h$ (hidrostática): $p = p_0 + \delta \cdot g \cdot h$, donde $p_0$ es la presión en la superficie (o atmosférica si está abierto al aire).
- Presión manométrica (sin contar la atmosférica): $p_{man} = \delta \cdot g \cdot h$.
- 1 atm = 1,013 × 10⁵ Pa = 760 mmHg.
- Principio de Pascal (prensa hidráulica): $\dfrac{F_1}{A_1} = \dfrac{F_2}{A_2}$ (misma presión transmitida a todo el fluido).
- Empuje (principio de Arquímedes): $E = \delta_{líquido} \cdot V_{sumergido} \cdot g$ — el empuje es el peso del volumen de líquido desplazado.
- Cuerpo **totalmente sumergido y apoyado en el fondo**: $E + N = P \Rightarrow N = P - E$ (si N > 0, el cuerpo se hunde).
- Cuerpo **flotando** (equilibrio): $E = P \Rightarrow \delta_{líquido}\cdot V_{sumergido}\cdot g = m_{cuerpo}\cdot g$ → el volumen sumergido depende de la relación de densidades: $\dfrac{V_{sumergido}}{V_{total}} = \dfrac{\delta_{cuerpo}}{\delta_{líquido}}$.
- Peso aparente (cuerpo sumergido con tensión): $Tensión = Peso - Empuje$.
- Vasos comunicantes con el mismo líquido: igual altura en ambas ramas. Con líquidos distintos: las alturas son inversamente proporcionales a la densidad.

## 4. Cinemática en una dimensión ⭐
- MRU (velocidad constante): $x = x_0 + v\cdot t$.
- MRUV (aceleración constante):
  $$x = x_0 + v_0 t + \tfrac{1}{2}at^2 \qquad v_f = v_0 + at \qquad v_f^2 - v_0^2 = 2a(x-x_0)$$
- Caída libre / tiro vertical: mismo MRUV pero con $a = \pm g$ (definir signo según el sistema de referencia elegido).
  - Caída libre desde el reposo: $h = \tfrac{1}{2}gt^2$, $v_f = g\cdot t$.
  - Tiro vertical hacia arriba: sube hasta $v=0$, luego cae; el tiempo de subida y bajada (hasta la misma altura) son iguales.
- Problemas de encuentro: plantear $x_A(t) = x_B(t)$ y despejar el tiempo de encuentro $t_e$.
- En gráficos x-t: la pendiente es la velocidad. En gráficos v-t: la pendiente es la aceleración y el área bajo la curva es el desplazamiento.

## Constantes y datos frecuentes
- $g = 9,80\ m/s^2$ (siempre indicado en el enunciado).
- $\delta_{agua} = 1,00 \times 10^3\ kg/m^3$ (agua dulce); $\delta_{agua\ de\ mar} \approx 1,02\text{-}1,03 \times 10^3\ kg/m^3$.
- 1 atm = 1,013 × 10⁵ Pa.
- Resultados finales: **3 cifras significativas + unidades** (regla fija de la cátedra Torti).
