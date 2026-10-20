import csv
import time
import random
import matplotlib.pyplot as plt

ARCHIVO = "peliculas.csv"   # el CSV descargado de Kaggle
COLUMNA = "title"           # nombre de la columna con los títulos


class Peliculas:
    """Lee el CSV y guarda los títulos en una lista."""

    def __init__(self, archivo, columna):
        self.titulos = []
        with open(archivo, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                if fila[columna] != "":
                    self.titulos.append(fila[columna])
        random.shuffle(self.titulos)  # mezclar para que no estén ordenados
        print("Títulos cargados:", len(self.titulos))


class Buscador:
    """Dos formas de buscar un título."""

    def buscar_en_lista(self, lista, objetivo):
        # O(n): revisa uno por uno
        for titulo in lista:
            if titulo == objetivo:
                return True
        return False

    def buscar_en_set(self, conjunto, objetivo):
        # O(1): va directo
        return objetivo in conjunto


class Ordenador:
    """Dos formas de ordenar una lista."""

    def bubble_sort(self, lista):
        # O(n²): dos ciclos anidados
        a = lista.copy()
        n = len(a)
        for i in range(n):
            for j in range(n - 1 - i):
                if a[j] > a[j + 1]:
                    temporal = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = temporal
        return a

    def ordenar_python(self, lista):
        # sorted() de Python: O(n log n)
        return sorted(lista)


class Experimento:
    """Mide los tiempos y hace las gráficas."""

    def __init__(self, titulos):
        self.titulos = titulos
        self.buscador = Buscador()
        self.ordenador = Ordenador()

    def probar_busqueda(self):
        tamanos = [1000, 5000, 10000, 50000, 100000]
        tiempos_lista = []
        tiempos_set = []
        usados = []

        for n in tamanos:
            if n > len(self.titulos):
                continue
            datos = self.titulos[:n]
            conjunto = set(datos)

            # 100 títulos que sí están y 100 que no (peor caso)
            consultas = random.sample(datos, 100)
            for i in range(100):
                consultas.append("no_existe_" + str(i))

            inicio = time.perf_counter()
            for q in consultas:
                self.buscador.buscar_en_lista(datos, q)
            t_lista = time.perf_counter() - inicio

            inicio = time.perf_counter()
            for q in consultas:
                self.buscador.buscar_en_set(conjunto, q)
            t_set = time.perf_counter() - inicio

            usados.append(n)
            tiempos_lista.append(t_lista)
            tiempos_set.append(t_set)
            print("n =", n, "| lista:", round(t_lista, 4), "s | set:", round(t_set, 6), "s")

        plt.figure()
        plt.plot(usados, tiempos_lista, "o-", label="Lista O(n)")
        plt.plot(usados, tiempos_set, "s-", label="Set O(1)")
        plt.xlabel("n (cantidad de datos)")
        plt.ylabel("Tiempo (s)")
        plt.title("Búsqueda: lista vs set")
        plt.legend()
        plt.grid(True)
        plt.savefig("grafica_busqueda.png")

    def probar_ordenamiento(self):
        tamanos = [500, 1000, 2000, 4000]
        tiempos_bubble = []
        tiempos_python = []
        usados = []

        for n in tamanos:
            if n > len(self.titulos):
                continue
            datos = self.titulos[:n]

            inicio = time.perf_counter()
            self.ordenador.bubble_sort(datos)
            t_bubble = time.perf_counter() - inicio

            inicio = time.perf_counter()
            self.ordenador.ordenar_python(datos)
            t_python = time.perf_counter() - inicio

            usados.append(n)
            tiempos_bubble.append(t_bubble)
            tiempos_python.append(t_python)
            print("n =", n, "| bubble:", round(t_bubble, 4), "s | sorted:", round(t_python, 6), "s")

        plt.figure()
        plt.plot(usados, tiempos_bubble, "o-", label="Bubble sort O(n²)")
        plt.plot(usados, tiempos_python, "s-", label="sorted() O(n log n)")
        plt.xlabel("n (cantidad de datos)")
        plt.ylabel("Tiempo (s)")
        plt.title("Ordenamiento: bubble sort vs sorted")
        plt.legend()
        plt.grid(True)
        plt.savefig("grafica_ordenamiento.png")


# ---------- Programa principal ----------
peliculas = Peliculas(ARCHIVO, COLUMNA)
experimento = Experimento(peliculas.titulos)

print("\n--- Búsqueda ---")
experimento.probar_busqueda()

print("\n--- Ordenamiento ---")
experimento.probar_ordenamiento()

plt.show()
