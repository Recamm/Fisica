# Unidad: Estática (equilibrio de cuerpo rígido)

Aparece en **todas** las variantes del parcial como ejercicio 2 (torque/momento) y suele combinarse con hidrostática en el ejercicio 3 (contrapesos).

## Método fijo para resolver cualquier problema de estática
1. Aislar el cuerpo y dibujar el **diagrama de cuerpo libre (DCL)**: todas las fuerzas externas (peso, tensiones, normales, empuje si hay líquido).
2. Elegir un sistema de ejes (x horizontal, y vertical).
3. Si las fuerzas son concurrentes (se cruzan en un punto): plantear $\sum F_x = 0$ y $\sum F_y = 0$.
4. Si hay cuerpos extendidos (barras, tablas, grúas): además plantear $\sum M_O = 0$ (momentos), eligiendo O en un apoyo para eliminar una incógnita.
5. Momento de una fuerza: $M = F \cdot d$, con $d$ = distancia perpendicular entre el punto O y la recta de acción de la fuerza.
6. Resolver el sistema de ecuaciones.

## Ejercicios resueltos reales (de los parciales)

### 1) Tabla que bascula (torque con 2 pesos + tensión de cuerda)
Persona de 75,0 kg parada en el extremo de una tabla de 20,0 kg y 3,00 m, que bascula en un punto a 1,00 m del extremo izquierdo. La cuerda forma 20,0° con la vertical.

Tomando momentos respecto del punto de apoyo (a):
$$75{,}0\cdot9{,}80\cdot2\ m + 20{,}0\cdot9{,}80\cdot0{,}5\ m - T\cos(20°)\cdot1\ m = 0 \Rightarrow T = 1{,}67\times10^3\ N$$

*Patrón:* peso de la persona y peso propio de la tabla generan momentos en un sentido; la tensión de la cuerda genera momento en sentido contrario. Todo respecto del punto de apoyo/bisagra.

### 2) Grúa levantando un auto (torque)
Auto de 1350 kg, centro de gravedad a 1,80 m del eje trasero, distancia total 3,50 m.

Momentos respecto del punto de apoyo de la rueda trasera:
$$1350\cdot9{,}80\cdot\cos(30°)\cdot1{,}80 - T\cdot\cos(30°)\cdot3{,}50 = 0 \Rightarrow T = 6{,}80\times10^3\ N$$

Luego, equilibrio de fuerzas verticales: $N + T - P = 0 \Rightarrow N = P - T = 6{,}43\times10^3\ N$.

*Patrón:* primero momentos para hallar la tensión/fuerza incógnita, después $\sum F_y=0$ para la normal.

### 3) Carros con poleas en plano inclinado (equilibrio de fuerzas, sin momento)
Carro B (12,5 kg) cuelga y tira de carro A (25,0 kg) sobre un plano inclinado a 45,0°, mediante una polea. Una persona tira de otra cuerda.

Equilibrio del carro B: $T_2 - P_B = 0 \Rightarrow T_2 = 122{,}5\ N$.
Equilibrio del carro A a lo largo del plano: $T_1 - T_2 - m_A g \sin(45°) = 0 \Rightarrow T_1 = 296\ N$.

*Patrón:* cuando hay poleas, conviene analizar cada cuerpo por separado con su propio DCL, en la dirección paralela a la superficie de contacto.

### 4) Líneas de pesca (equilibrio de fuerzas concurrentes en 2D)
Dos cuerdas en ángulo (30° y 45° respecto de la vertical) sostienen un peso. Se conoce la tensión de una.
$$\sum F_x=0: T_{hijo}\sin(45°) - T_{padre}\sin(30°) = 0$$
$$\sum F_y=0: T_{hijo}\cos(45°) + T_{padre}\cos(30°) - P = 0$$
Se despeja primero $T_{hijo}$ de la ecuación en x, se reemplaza en y, y se obtiene el peso (y la masa).

## Errores comunes a evitar
- Olvidar que el peso de la barra/tabla actúa en su **centro de gravedad** (punto medio si es homogénea), no en un extremo.
- Elegir mal el punto de momentos (siempre conviene un punto de apoyo, así su fuerza desaparece de la ecuación).
- Mezclar signos de momentos horario/antihorario sin fijar una convención al principio.
- No dibujar el DCL pedido explícitamente (tiene puntaje propio, aunque parezca "obvio").
