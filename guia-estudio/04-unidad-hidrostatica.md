# Unidad: Hidrostática

Es el ejercicio con **más puntaje** en todas las variantes del parcial analizado (3-4 puntos), y a veces se combina con estática (estatua sumergida + contrapeso en palanca).

## Ideas clave (en orden de uso)
1. **Identificar el estado del cuerpo**: ¿totalmente sumergido y apoyado en el fondo? ¿flotando con una parte afuera? ¿sumergido y sostenido por una cuerda?
2. Cada estado tiene su propia ecuación de equilibrio (ver formulario), pero siempre parte de: **fuerzas que actúan = peso, empuje, normal y/o tensión**, y $\sum F = 0$.
3. El empuje siempre se calcula con el volumen **desplazado** (= volumen sumergido), NO el volumen total del cuerpo (salvo que esté totalmente sumergido).
4. Presión a profundidad $h$: sumar siempre la presión en la superficie (atmosférica o la que corresponda) más $\delta g h$.

## Ejercicios resueltos reales (de los parciales)

### 1) Esfera sumergida y apoyada en el fondo (empuje + normal)
Esfera de aluminio (δ=2,70×10³ kg/m³) de 3,00 cm de diámetro, apoyada en el fondo de un recipiente con alcohol (δ=7,89×10² kg/m³).
- Masa: $m = V\cdot\delta_{esfera} = \frac{4}{3}\pi(0{,}015)^3\cdot2{,}70\times10^3 = 38{,}2\ g$
- Empuje: $E = V\cdot\delta_{líquido}\cdot g = \frac{4}{3}\pi(0{,}015)^3\cdot7{,}89\times10^2\cdot9{,}80 = 0{,}109\ N$
- Normal (equilibrio $E+N-P=0$): $N = P - E = m\cdot g - E = 0{,}265\ N$

### 2) Presión a profundidad + porcentaje sumergido (buceador)
A 214 m de profundidad en agua de mar (δ=1,025 g/cm³), presión atmosférica 1,013×10⁵ Pa.
$$\frac{p_{214m}}{p_{atm}} = \frac{1{,}013\times10^5 + 1025\cdot9{,}80\cdot214}{1{,}013\times10^5} = 22{,}2\ \text{veces}$$
Porcentaje del cuerpo sumergido (equilibrio $E=P$, densidad del buceador 0,960 g/cm³):
$$\frac{V_{sumergido}}{V_{total}} = \frac{\delta_{buceador}}{\delta_{agua}} = 93{,}7\%$$

### 3) Cubo que flota (presión en la base + masa)
Cubo de 4,00 cm de arista flotando en aceite (δ=0,950 g/cm³), emergiendo 1/4 de su volumen (es decir, 3/4 sumergido → profundidad sumergida = 3,00 cm).
- Presión en la base: $p = \delta g h = 950\cdot9{,}80\cdot0{,}0300 = 279\ Pa$
- Masa (equilibrio $E=P$): $m = V_{sumergido}\cdot\delta_{aceite} = 45{,}6\ g$

### 4) Estatua sumergida + contrapeso en palanca (combina hidrostática + estática)
Estatua de 160 kg, granito (δ=2,80 g/cm³), sumergida en agua de mar (δ=1,025 g/cm³), sostenida por una cuerda conectada a una palanca con contrapeso.
- Equilibrio de la estatua: $T + E - P = 0 \Rightarrow T = P - E = 994\ N$ (usando $E = \frac{m}{\delta_{estatua}}\cdot\delta_{agua}\cdot g$)
- Equilibrio de momentos en la palanca (brazo 1,00 m del contrapeso vs 3,00 m de la tensión):
$$1{,}00\cdot m_{contrapeso}\cdot g = 3{,}00\cdot T \Rightarrow m_{contrapeso} = 304\ kg$$

*Patrón:* primero resolver la parte de hidrostática (hallar la tensión de la cuerda como si fuera un cuerpo sumergido en equilibrio), y usar ese resultado como dato de entrada para un problema de estática (momentos en la palanca).

## Errores comunes a evitar
- Usar el volumen total del cuerpo para el empuje cuando en realidad está parcialmente sumergido (flotando).
- Olvidar sumar la presión atmosférica/de superficie al calcular presión absoluta a una profundidad (la presión manométrica NO la incluye).
- Confundir densidad del cuerpo con densidad del líquido en la fórmula del empuje (el empuje SIEMPRE usa la densidad del líquido).
