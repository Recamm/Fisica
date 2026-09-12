# Guía de estudio intensiva — Física UBA XXI (2 días)

Empezá por [guia-estudio/00-cronograma.md](guia-estudio/00-cronograma.md): ahí está el plan hora por hora y el resumen del hallazgo clave (cómo es realmente el parcial).

## Índice
1. [guia-estudio/00-cronograma.md](guia-estudio/00-cronograma.md) — plan de estudio para 2 días
2. [guia-estudio/01-formulario.md](guia-estudio/01-formulario.md) — todas las fórmulas en un solo lugar
3. [guia-estudio/02-unidad-vectores-medicion.md](guia-estudio/02-unidad-vectores-medicion.md) — Medición (repaso corto) + Vectores: resumen + ejercicios resueltos
4. [guia-estudio/03-unidad-estatica.md](guia-estudio/03-unidad-estatica.md) — Estática: resumen + ejercicios resueltos
5. [guia-estudio/04-unidad-hidrostatica.md](guia-estudio/04-unidad-hidrostatica.md) — Hidrostática: resumen + ejercicios resueltos
6. [guia-estudio/05-unidad-cinematica.md](guia-estudio/05-unidad-cinematica.md) — Cinemática en una dimensión: resumen + ejercicios resueltos
7. [guia-estudio/06-banco-ejercicios-parciales.md](guia-estudio/06-banco-ejercicios-parciales.md) — ejercicios reales de parciales para practicar
8. [guia-estudio/07-simulacro-final.md](guia-estudio/07-simulacro-final.md) — simulacro cronometrado tipo examen

### Teoría a fondo (explicación extensa de cada tema, para aprender desde cero)
Si los archivos 02-05 te resultan muy resumidos (son ejercicios + tips, no explican el tema en sí), empezá por estos: explican con palabras simples, intuición y el "por qué" de cada fórmula, antes de resolver ejercicios.

9. [guia-estudio/08-teoria-vectores-medicion.md](guia-estudio/08-teoria-vectores-medicion.md) — explicación extensa de Medición y Vectores
10. [guia-estudio/09-teoria-estatica.md](guia-estudio/09-teoria-estatica.md) — explicación extensa de Estática
11. [guia-estudio/10-teoria-hidrostatica.md](guia-estudio/10-teoria-hidrostatica.md) — explicación extensa de Hidrostática
12. [guia-estudio/11-teoria-cinematica.md](guia-estudio/11-teoria-cinematica.md) — explicación extensa de Cinemática en una dimensión

## Qué se descubrió al analizar los parciales reales
Los 9 PDF de la carpeta `parciales/` (`67_compressed.pdf` + los 8 de `resueltos/`) resultaron ser, en realidad, **8 "temas" (variantes) del mismo Primer Parcial**, tomado el 07/05/2026 por la cátedra Torti — no son 9 exámenes de fechas distintas. Comparar las 8 variantes lado a lado permitió detectar el formato exacto y fijo del examen:

- **Siempre son 4 ejercicios, en el mismo orden y con el mismo tipo de consigna** (solo cambian los números y el contexto de la historia):
  1. **Cinemática 1D** (2 pts) — siempre uno de estos 4 patrones: caída libre simple dado el tiempo, caída libre simple dada la altura, caída libre + tramo a velocidad constante (paracaidista), o encuentro a velocidad constante (tipo tortuga y liebre).
  2. **Estática** (2-3 pts) — equilibrio de un cuerpo rígido con torque: una tabla que bascula, una grúa levantando un auto, carros unidos por cuerdas y poleas en un plano inclinado, o líneas que sostienen un peso en ángulo. Siempre piden además el diagrama de cuerpo libre (DCL), con puntaje propio.
  3. **Hidrostática** (3-4 pts, el de mayor puntaje) — esfera sumergida y apoyada en el fondo (empuje + normal), presión a una profundidad dada, un cuerpo que flota (% del volumen sumergido), o un cuerpo sumergido sostenido por una cuerda combinado con una palanca y contrapeso (mezcla hidrostática + estática).
  4. **Vectores** (2-3 pts) — suma o resta de vectores, módulo y ángulo del resultado, producto escalar y producto vectorial (con dirección y sentido).
- **Lo que NO aparece como ejercicio propio:** "Medición" (cifras significativas, notación científica, conversión de unidades) de la Semana 1. Es la base para expresar cualquier resultado (el examen siempre exige 3 cifras significativas y unidades), pero no hay un ejercicio dedicado a ese tema.
- **Reglas fijas del examen** (se repiten en las 8 variantes): usar $g=9{,}80\ m/s^2$, expresar resultados con 3 cifras significativas y unidades, y el diagrama de cuerpo libre se pide explícitamente y puntúa aparte.

Esta comparación es la que definió las prioridades del [guia-estudio/00-cronograma.md](guia-estudio/00-cronograma.md) (más tiempo a Hidrostática y Estática, que suman más puntos) y el contenido del [guia-estudio/06-banco-ejercicios-parciales.md](guia-estudio/06-banco-ejercicios-parciales.md) y el [guia-estudio/07-simulacro-final.md](guia-estudio/07-simulacro-final.md), armados a partir de estos mismos patrones reales.

## Fuente de este material
Se extrajo texto de los 19 PDF del workspace (script en `_extraido/extract_pdfs.py`) y se analizaron los 8 "temas" del Primer Parcial real (07/05/2026, cátedra Torti) para detectar el formato exacto del examen: siempre 4 ejercicios (Cinemática 1D, Estática, Hidrostática, Vectores), con "Medición" como base pero sin ejercicio propio.
