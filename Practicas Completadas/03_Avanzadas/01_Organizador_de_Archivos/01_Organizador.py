import os
import shutil

RUTA_ORIGEN = "./Practicas Completadas/03_Avanzadas/01_Organizador_de_Archivos/Archivos/carpeta_origen/"
RUTA_DESTINO = "./Practicas Completadas/03_Avanzadas/01_Organizador_de_Archivos/Archivos/carpeta_destino/"


def obtener_archivos():
    """Obtiene todos los archivos dentro de la carpeta."""
    return os.listdir(RUTA_ORIGEN)


def obtener_extension(archivo: str) -> str:
    """Devuelve la extensión de un archivo a partir de su nombre."""

    _, extension = os.path.splitext(archivo)
    return extension[1:] if extension else "sin extensión"


def crear_carpeta(extension: str):
    """Crea una carpeta para la extensión especificada."""

    carpeta = os.path.join(RUTA_DESTINO, extension)

    if not os.path.exists(carpeta):
        os.makedirs(carpeta)


def organizar_archivos():
    """Organiza los archivos en carpetas según su extensión."""
    print("Obteniendo archivos...")
    try:
        archivos = obtener_archivos()
        if not archivos:
            print("No hay archivos para organizar.")
            return
    except Exception as e:
        print(f"Error al obtener archivos: {e}")
        return

    extensiones = set(obtener_extension(archivo) for archivo in archivos)
    print(f"Extensiones encontradas: {extensiones}")

    print("Creando carpetas para cada extensión...")
    try:
        for extension in extensiones:
            crear_carpeta(extension)
        print("Carpetas creadas.")
    except Exception as e:
        print(f"Error al crear carpetas: {e}")
        return

    try:
        for archivo in archivos:
            extension = obtener_extension(archivo)
            origen = os.path.join(RUTA_ORIGEN, archivo)
            destino = os.path.join(RUTA_DESTINO, extension, archivo)
            shutil.move(origen, destino)
            print(f"Movido: {archivo} -> {extension}/")
        print("Organización completada.")
    except Exception as e:
        print(f"Error al mover archivos: {e}")


def eliminar_carpetas():
    """Elimina las carpetas creadas para organizar los archivos."""

    extensiones = set(obtener_extension(archivo) for archivo in obtener_archivos())

    for extension in extensiones:
        carpeta = os.path.join(RUTA_DESTINO, extension)
        if os.path.exists(carpeta):
            shutil.rmtree(carpeta)


def revertir_organizacion():
    """Revierte la organización moviendo los archivos de vuelta a la carpeta original."""
    print("Revirtiendo organización...")
    try:
        for root, dirs, files in os.walk(RUTA_DESTINO):
            for file in files:
                origen = os.path.join(root, file)
                destino = os.path.join(RUTA_ORIGEN, file)
                shutil.move(origen, destino)
                print(f"Movido: {file} -> carpeta_origen/")
        print("Eliminando carpetas vacías...")
        eliminar_carpetas()
        print("Reversión completada.")
    except Exception as e:
        print(f"Error al revertir organización: {e}")


organizar_archivos()

# Para revertir el proceso de organización, descomenta la siguiente línea.
# revertir_organizacion()
