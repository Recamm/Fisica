# Unidad: Medición + Vectores (Magnitudes Físicas)

## Parte A — Medición (repaso rápido, 20-30 min)
No aparece como ejercicio propio en el parcial analizado, pero define cómo tenés que entregar TODOS los resultados: **3 cifras significativas y unidades**.

- Notación científica: mover el punto decimal y contar cuántos lugares te movés → ese número va como exponente de 10.
  - Ej: `328,65` → `3,2865 x 10²`
- Cifras significativas al sumar: el resultado tiene tantos decimales como el término menos preciso.
  - Ej: `1,80 m + 142,5 cm + 5,34x10⁵ µm` → convertir todo a la misma unidad y redondear según el término menos preciso → **3,76 m**.
- Cifras significativas al multiplicar/dividir: el resultado tiene tantas cifras significativas como el factor con menos cifras.
- Análisis dimensional: si te dan una fórmula rara (ej. $Vol = \pi r^3 h$), fijate si las dimensiones cierran. Un volumen tiene que dar $[L]^3$; si la fórmula da $[L]^4$, está mal.

**Ejercicio resuelto (de `Semana 1/Actividades`):**
> Sume 1,80 metros + 142,5 centímetros + 5,34×10⁵ micrómetros.
> Conversión: 1,80 m + 1,425 m + 0,534 m = 3,759 m → redondeado a la precisión del término menos preciso (1,80 m tiene 2 decimales) → **3,76 m**.

## Parte B — Vectores (1 h, esto SÍ es el ejercicio 4 de todos los parciales)

### Método fijo para resolver cualquier ejercicio de vectores
1. Descomponer cada vector en componentes x e y: $A_x = A\cos\theta$, $A_y = A\sin\theta$.
2. Para sumar/restar: operar componente a componente.
3. Para el módulo del resultado: Pitágoras $\sqrt{R_x^2+R_y^2}$.
4. Para el ángulo: $\arctan(R_y/R_x)$, ajustando el cuadrante según los signos de $R_x, R_y$.
5. Producto escalar: $A_xB_x + A_yB_y$ → da un escalar (puede ser negativo).
6. Producto vectorial (en el plano xy): $(A_xB_y - A_yB_x)\hat{k}$ → da un vector perpendicular al plano; el signo indica si es $+\hat{k}$ (sale de la hoja) o $-\hat{k}$ (entra a la hoja).

### Ejercicios resueltos reales (sacados de los parciales)
**1) Suma y ángulo de fuerzas** — *A = 32,0 N a 30,0° sobre la horizontal; B = 40,0 N a 35,0° de otro eje.*
$$A_x = 32{,}0\cos(30{,}0°),\quad A_y = 32{,}0\sin(30{,}0°)$$
$$B_x = 40{,}0\sin(35{,}0°),\quad B_y = 40{,}0\cos(35{,}0°)$$
$$|\vec{A}+\vec{B}| = 70{,}3\ N \qquad \text{ángulo} = 43{,}9°$$

**2) Producto vectorial** — mismos vectores, ángulo entre ellos 25°:
$$|\vec{A}\times\vec{B}| = 32{,}0 \cdot 40{,}0 \cdot \sin(25°) = 541\ N^2\,\hat{k}$$

**3) Vectores dados por componentes** — *A = (4,00 ; 6,00), B = (2,00 ; -1,00).*
- Producto escalar: $A\cdot B = 4{,}00\cdot2{,}00 + 6{,}00\cdot(-1{,}00) = 2{,}00$
- Módulos: $|A|=7{,}21$, $|B|=2{,}24$
- Ángulo entre ambos: $\arccos(2{,}00/(7{,}21\cdot2{,}24)) = 82{,}9°$
- Módulo de $(A+B)$: $\sqrt{(6{,}00)^2+(5{,}00)^2} = 7{,}81$

### Errores comunes a evitar
- Confundir el ángulo "respecto del eje x" con "respecto del eje y" (leer bien el enunciado, cambia si usás seno o coseno).
- Olvidar el signo al restar vectores ($\vec{A}-\vec{B} = \vec{A}+(-\vec{B})$).
- En el producto vectorial, olvidarse de indicar la dirección ($\hat{k}$ o $-\hat{k}$), que tiene puntaje propio.
