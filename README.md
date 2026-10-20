# Complejidad algorítmica y análisis Big-O con datos de películas

## Descripción

Proyecto del curso **Estructura de Datos** (Equipo 6: Complejidad algorítmica y análisis Big-O).

El objetivo es comprobar de forma experimental que la teoría de la complejidad se cumple en la práctica. Para ello se comparan dos problemas con distintas soluciones y se mide cuánto tarda cada una cuando la cantidad de datos (n) crece:

1. **Búsqueda de un título:** lista O(n) contra set O(1).
2. **Ordenamiento de títulos:** bubble sort O(n²) contra `sorted()` de Python O(n log n).

## Dataset

- **Fuente:** [PEGAR AQUÍ EL LINK DE KAGGLE DEL DATASET USADO]
- **Descripción:** conjunto de películas con información como título, año y calificación. Se usa la columna de títulos (`title`) como datos de prueba, con decenas de miles de registros, para poder medir cómo cambia el tiempo cuando n crece.

## Tecnologías

- Python 3
- `csv`, `time` y `random` (librería estándar)
- `matplotlib` para las gráficas

## Implementación

El código está organizado con programación orientada a objetos en el archivo `main_poo.py`:

| Clase | Qué hace | Complejidad |
|---|---|---|
| `Peliculas` | Lee el CSV y guarda los títulos en una lista | Tiempo O(n), espacio O(n) |
| `Buscador` | `buscar_en_lista`: recorre uno por uno | Peor caso O(n), mejor caso Ω(1) |
| `Buscador` | `buscar_en_set`: acceso directo por tabla hash | O(1) en promedio |
| `Ordenador` | `bubble_sort`: dos ciclos anidados | O(n²) |
| `Ordenador` | `ordenar_python`: usa `sorted()` | O(n log n) |
| `Experimento` | Ejecuta cada algoritmo con tamaños crecientes, mide el tiempo con `time.perf_counter()` y genera las gráficas | - |

**Detalles del experimento:**

- **Búsqueda:** n = 1,000, 5,000, 10,000, 50,000 y 100,000. Se hacen 200 consultas por tamaño: 100 títulos que existen y 100 que no existen (peor caso para la lista).
- **Ordenamiento:** n = 500, 1,000, 2,000 y 4,000, porque bubble sort es muy lento con tamaños grandes.

## Ejecución

1. Descargar el dataset desde el link de la sección *Dataset* y guardarlo como `peliculas.csv` en la misma carpeta que `main_poo.py`.
2. Instalar la librería de gráficas:

```bash
pip install matplotlib
```

3. Ejecutar el proyecto:

```bash
python main_poo.py
```

Si la columna de títulos del CSV no se llama `title`, cambiar la variable `COLUMNA` al inicio de `main_poo.py`.

## Resultados

El programa imprime una tabla de tiempos por consola y guarda dos gráficas:

- `grafica_busqueda.png`
- `grafica_ordenamiento.png`

**Resultados esperados según la teoría:**

- En la búsqueda, el tiempo de la lista crece de forma lineal con n, mientras que el del set se mantiene casi constante.
- En el ordenamiento, bubble sort crece de forma cuadrática (al duplicar n, el tiempo se multiplica aproximadamente por 4), mientras que `sorted()` casi no cambia.

**Resultados obtenidos:** [COMPLETAR DESPUÉS DE EJECUTAR EL CÓDIGO: pegar las gráficas y una tabla corta con los tiempos reales, y comentar si coinciden con lo esperado.]

## Autores

- [Nombre 1]
- [Nombre 2]
- [Nombre 3]
