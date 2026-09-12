# Cronograma de estudio — 2 días (4-6 h/día)

## Hallazgo clave que define este cronograma
Los 9 PDFs de `parciales/` (67_compressed + los 8 `resueltos/`) son en realidad **8 "temas" (variantes) del mismo Primer Parcial**, tomado el 07/05/2026 por la cátedra Torti. Todos comparten EXACTAMENTE la misma estructura de 4 ejercicios:

| # | Tema | Puntaje típico | Variantes vistas |
|---|------|-----------------|-------------------|
| 1 | **Cinemática 1D** | 2 pts | caída libre (altura/rapidez dado t), granizo (rapidez dada h), paracaidista (caída libre + tramo a velocidad constante), tortuga-liebre (encuentro a velocidad constante) |
| 2 | **Estática** (equilibrio de cuerpo rígido) | 2-3 pts | tabla que bascula (torque), grúa levantando auto (torque), carros con poleas en plano inclinado, líneas de pesca en ángulo (padre e hijo) — siempre piden diagrama de cuerpo libre (DCL) |
| 3 | **Hidrostática** | 3-4 pts | esfera sumergida (empuje + normal en el fondo), presión a profundidad (buceador), cubo que flota (% sumergido), estatua sumergida + contrapeso en palanca (combina con estática) |
| 4 | **Vectores** | 2-3 pts | suma/resta de vectores, módulo y ángulo, producto escalar, producto vectorial (dirección con mano derecha) |

**Conclusión:** el examen NO evalúa directamente "Medición" (cifras significativas/notación científica de Semana 1) como ejercicio propio — son la base para expresar resultados (3 cifras significativas, siempre piden unidades), pero no aparece como ejercicio dedicado. Por eso baja de prioridad.

**Prioridad para las 8-12 horas disponibles (de mayor a menor):**
1. Hidrostática (más puntaje, mezcla con estática)
2. Estática (torque/equilibrio, siempre con DCL)
3. Vectores (siempre el ejercicio 4, mecánico si se domina el método)
4. Cinemática 1D (siempre el ejercicio 1, patrones muy repetibles)
5. Medición (repaso corto: cifras significativas, notación científica — no es ejercicio de parcial pero afecta cómo entregás resultados)

Cada bloque de unidad tiene 2 pasos: primero **leer la teoría a fondo** (para entender de dónde sale cada fórmula, no solo memorizarla) y después **resolver los ejercicios resueltos** de la guía resumen. Si ya entendiste el concepto, podés saltar directo a los ejercicios.

---

## Día 1 (~5 h 30 min) — Bases + Estática + Hidrostática

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| 1 | 15 min | [08-teoria-vectores-medicion.md](08-teoria-vectores-medicion.md) (Parte A) — entender cifras significativas y notación científica |
| 2 | 15 min | [02-unidad-vectores-medicion.md](02-unidad-vectores-medicion.md) (Parte A) — resolver el ejercicio de medición |
| 3 | 40 min | [08-teoria-vectores-medicion.md](08-teoria-vectores-medicion.md) (Parte B) — entender vectores: por qué componentes, producto escalar y vectorial |
| 4 | 30 min | [02-unidad-vectores-medicion.md](02-unidad-vectores-medicion.md) (Parte B) — resolver los 3 ejercicios de vectores |
| 5 | 15 min | Descanso |
| 6 | 50 min | [09-teoria-estatica.md](09-teoria-estatica.md) — entender fuerzas concurrentes/no concurrentes, momento de una fuerza, por qué hace falta $\sum M=0$ |
| 7 | 1 h | [03-unidad-estatica.md](03-unidad-estatica.md) — resolver los 4 ejercicios resueltos (tabla que bascula, grúa, plano inclinado, líneas de pesca) |
| 8 | 15 min | Descanso |
| 9 | 45 min | [10-teoria-hidrostatica.md](10-teoria-hidrostatica.md) — entender presión, Pascal, empuje y los 3 casos (apoyado, flotando, sostenido por cuerda) |
| 10 | 45 min | [04-unidad-hidrostatica.md](04-unidad-hidrostatica.md) — resolver los 4 ejercicios resueltos |

Cierre del día: releer una vez el [01-formulario.md](01-formulario.md) completo (10-15 min), sin resolver nada, solo para que las fórmulas "entren por los ojos".

## Día 2 (~5 h) — Cinemática + Simulacro + Repaso final

| Bloque | Duración | Contenido |
|--------|----------|-----------|
| 1 | 40 min | [11-teoria-cinematica.md](11-teoria-cinematica.md) — entender MRU, MRUV, caída libre/tiro vertical y encuentro |
| 2 | 50 min | [05-unidad-cinematica.md](05-unidad-cinematica.md) — resolver los ejercicios resueltos (los 4 patrones típicos de parcial) |
| 3 | 15 min | Descanso |
| 4 | 1 h 30 min | [06-banco-ejercicios-parciales.md](06-banco-ejercicios-parciales.md) — resolver ejercicios reales de parciales SIN mirar la solución primero, después corregir |
| 5 | 15 min | Descanso |
| 6 | 1 h 30 min | [07-simulacro-final.md](07-simulacro-final.md) — simulacro cronometrado (1,5 h, igual que el examen real) en condiciones de examen: sin apuntes, con calculadora |
| 7 | 20 min | Corregir el simulacro contra las soluciones, repasar SOLO lo que salió mal, y releer el formulario una última vez |

Si vas corto de tiempo el día 2, el orden de prioridad para recortar es: banco de ejercicios (podés resolver menos de los que aparecen) antes que el simulacro (no te lo saltees, es tu mejor termómetro).

## Reglas de oro para el examen (repetidas en todas las variantes)
- Siempre usar **g = 9,80 m/s²** (lo indica el enunciado).
- Siempre expresar resultados con **3 cifras significativas y unidades**.
- Cuando piden "diagrama de cuerpo libre", dibujarlo aunque parezca trivial — tiene puntaje propio.
- En estática, elegir el centro de momentos en un punto donde se anule una incógnita (usualmente un apoyo).
- En hidrostática, identificar primero si el cuerpo está totalmente sumergido, apoyado en el fondo, o flotando parcialmente — cada caso cambia la ecuación de equilibrio.
