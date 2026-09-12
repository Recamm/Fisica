# Teoría a fondo — Hidrostática

Este archivo explica el "por qué" de cada concepto de hidrostática. Los ejercicios y el paso a paso resumido ya están en [04-unidad-hidrostatica.md](04-unidad-hidrostatica.md); acá está la explicación completa para entenderlo antes de practicar.

## ¿Qué estudia la hidrostática?
"Hidro" = agua, "estática" = quieto. Estudia los líquidos (o fluidos en general) que están en reposo, y qué fuerzas y presiones ejercen sobre los cuerpos sumergidos o flotando en ellos.

## Densidad
$$\delta = \frac{m}{V}$$
Es cuánta masa hay en cada unidad de volumen. Dos objetos del mismo tamaño pueden pesar muy distinto según su densidad (un cubo de plomo pesa mucho más que un cubo de telgopor del mismo tamaño). La densidad es la propiedad que determina si algo flota o se hunde en un líquido dado.

## Presión
$$p = \frac{F}{A}$$
Es la fuerza que actúa repartida sobre una superficie. La misma fuerza aplicada sobre una superficie chica genera más presión que sobre una superficie grande (por eso un cuchillo afilado corta mejor: concentra la fuerza en un área muy chica). La unidad en el sistema internacional es el Pascal ($1\ Pa = 1\ N/m^2$).

## Presión hidrostática (presión a una profundidad h)
Si estás sumergido en un líquido a una profundidad $h$, el líquido que está por encima tuyo "pesa" y ese peso genera presión adicional. La fórmula es:
$$p = p_0 + \delta \cdot g \cdot h$$
donde $p_0$ es la presión en la superficie del líquido (si está abierto al aire, es la presión atmosférica).

**Intuición:** cuanto más profundo estás, más columna de líquido tenés encima, y por lo tanto más presión sentís. Por eso a los buzos les cuesta respirar a mucha profundidad, y por eso los submarinos tienen que estar diseñados para resistir presiones enormes.

Un detalle importante: la presión **no depende de la forma del recipiente**, solo depende de la profundidad y de la densidad del líquido. Esto es lo que permite el fenómeno de los vasos comunicantes.

## Presión manométrica vs. presión absoluta
- **Presión absoluta:** incluye la presión atmosférica más la presión debida al líquido ($p = p_0 + \delta g h$).
- **Presión manométrica:** es solo la parte debida al líquido, sin contar la atmosférica ($p_{man} = \delta g h$). Es lo que marcan la mayoría de los manómetros (instrumentos de medición de presión), porque están calibrados para ignorar la presión atmosférica de fondo.

## Principio de Pascal (prensa hidráulica)
Cuando aplicás presión en algún punto de un líquido encerrado, esa presión se transmite **igual** a todos los puntos del líquido. Esto permite "amplificar" fuerzas: si tenés dos pistones de áreas distintas conectados por el mismo líquido,
$$\frac{F_1}{A_1} = \frac{F_2}{A_2}$$
Con una fuerza chica en el pistón chico, podés generar una fuerza mucho más grande en el pistón grande (así funcionan los elevadores hidráulicos de los talleres mecánicos, o los frenos hidráulicos de un auto).

## Principio de Arquímedes (empuje) — el concepto más importante de la unidad
Cuando un cuerpo está sumergido (total o parcialmente) en un líquido, el líquido lo empuja hacia arriba con una fuerza llamada **empuje**:
$$E = \delta_{líquido} \cdot V_{sumergido} \cdot g$$

**¿Por qué aparece esta fuerza?** Porque la presión del líquido aumenta con la profundidad. La cara de abajo del cuerpo sumergido está más profunda que la de arriba, así que recibe más presión desde abajo que la que recibe desde arriba. Esa diferencia de presiones, actuando sobre las distintas caras del cuerpo, genera una fuerza neta hacia arriba: eso es el empuje.

**Regla práctica para calcular el empuje:** el empuje es igual al **peso del volumen de líquido que el cuerpo desplaza** (no al peso del cuerpo). Si el cuerpo está totalmente sumergido, el volumen desplazado es el volumen total del cuerpo. Si está flotando con una parte afuera, el volumen desplazado es solo la parte sumergida.

## Los 3 casos posibles para un cuerpo en un líquido (identificar SIEMPRE cuál es antes de plantear ecuaciones)

### Caso 1: cuerpo totalmente sumergido y apoyado en el fondo
Actúan: peso (abajo), empuje (arriba), normal del fondo (arriba).
$$E + N = P \quad\Rightarrow\quad N = P - E$$
Si al calcular $N$ te da positivo, efectivamente el cuerpo se queda apoyado (más denso que el líquido). Si te diera negativo, en realidad el cuerpo flotaría (esto indica que el planteo del problema — o la suposición de que está apoyado — no es correcta).

### Caso 2: cuerpo flotando (parcialmente sumergido, en equilibrio)
Actúan: peso (abajo) y empuje (arriba), y se compensan exactamente:
$$E = P \quad\Rightarrow\quad \delta_{líquido}\cdot V_{sumergido}\cdot g = m_{cuerpo}\cdot g$$
De acá se obtiene una relación muy útil: la fracción del volumen que queda sumergida es igual a la relación entre densidades:
$$\frac{V_{sumergido}}{V_{total}} = \frac{\delta_{cuerpo}}{\delta_{líquido}}$$
Por ejemplo, el hielo flota en agua con aproximadamente el 90% de su volumen sumergido, porque su densidad es aproximadamente el 90% de la del agua.

### Caso 3: cuerpo sumergido y sostenido por una cuerda (no toca el fondo)
Actúan: peso (abajo), empuje (arriba), tensión de la cuerda (arriba, si el cuerpo tiende a hundirse):
$$T + E = P \quad\Rightarrow\quad T = P - E$$
Esto también se conoce como "peso aparente": un cuerpo sumergido en agua "pesa menos" (la balanza o la cuerda sienten menos fuerza) porque el empuje ayuda a sostenerlo.

## Vasos comunicantes
Si dos recipientes conectados contienen el **mismo** líquido, el líquido alcanza la **misma altura** en ambos recipientes (sin importar la forma de cada uno), porque la presión en la base tiene que ser igual en ambos lados. Si los recipientes tienen líquidos **distintos**, las alturas quedan relacionadas de forma inversamente proporcional a sus densidades (el líquido más denso forma una columna más baja).

## Cómo encarar cualquier problema de hidrostática, paso a paso
1. Identificar el estado del cuerpo: ¿totalmente sumergido y apoyado?, ¿flotando parcialmente?, ¿sumergido y sostenido por una cuerda?
2. Dibujar el diagrama de cuerpo libre con las fuerzas que correspondan a ese caso (peso siempre, empuje siempre que haya líquido, y normal o tensión según corresponda).
3. Plantear la ecuación de equilibrio ($\sum F = 0$) para ese caso particular.
4. Calcular el empuje usando el volumen realmente sumergido (no el total, salvo que lo esté).
5. Si hay una segunda parte del problema con una palanca o contrapeso, usar el resultado de la parte hidrostática (por ejemplo, la tensión) como dato de entrada para un problema de estática (equilibrio de momentos).

## Por qué este tema tiene tanto puntaje en el parcial
Porque combina conceptos (densidad, presión, empuje) que se pueden preguntar de muchas formas distintas (esferas que se hunden, cubos que flotan, presión a cierta profundidad, combinación con estática), y es un tema donde un solo error de concepto (por ejemplo, usar el volumen total en vez del sumergido) te hace fallar todo el ejercicio.
