import csv

RUTA_ARCHIVO = "./Practicas Completadas/03_Avanzadas/05_Analizador_CSV/Archivos/datos_productos.csv"


def leer_csv(ruta_archivo):
    """Lee un archivo CSV y devuelve una lista de diccionarios."""
    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector_csv = csv.DictReader(archivo)
        return [fila for fila in lector_csv]


def mostrar_productos(productos):
    """Muestra los productos en un formato legible."""
    for producto in productos:
        print(f"Nombre: {producto['Nombre']}, Precio: {producto['Precio']}")


def obtener_estadisticas(productos):
    """Calcula estadísticas básicas de los precios de los productos."""
    precios = [float(producto["Precio"]) for producto in productos]
    if not precios:
        return None, None, None
    promedio = sum(precios) / len(precios)
    maximo = max(precios)
    minimo = min(precios)
    return promedio, maximo, minimo


def ejecutar_analisis():
    """Función principal para ejecutar el análisis del CSV."""
    productos = leer_csv(RUTA_ARCHIVO)
    mostrar_productos(productos)
    promedio, maximo, minimo = obtener_estadisticas(productos)
    if promedio is not None:
        print("\nEstadísticas de Precios:")
        print(f"\nPromedio: {promedio:.2f}")
        print(f"Máximo: {maximo:.2f}")
        print(f"Mínimo: {minimo:.2f}\n")
    else:
        print("No se encontraron productos.")


ejecutar_analisis()
