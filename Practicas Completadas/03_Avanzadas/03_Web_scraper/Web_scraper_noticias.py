import os
import shutil
import requests
from bs4 import BeautifulSoup

URL = "https://www.elpais.com.uy/ultimas-noticias"
RUTA_ARCHIVO = "./Practicas Completadas/03_Avanzadas/03_Web_scraper/Archivos/"


def obtener_noticias(url: str):
    """Obtiene los títulos de las noticias desde la URL proporcionada."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        noticias = soup.find_all("div", class_="PromoBn")
        titulos = [noticia.find("a").get_text(strip=True) for noticia in noticias]
        return titulos
    except requests.RequestException as e:
        print(f"Error al obtener las noticias: {e}")
        return


def crear_archivo(ruta: str):
    """Crea el directorio para guardar los archivos si no existe."""
    try:
        if not os.path.exists(ruta):
            os.makedirs(ruta)
    except Exception as e:
        print(f"Error al crear el directorio: {e}")


def guardar_noticias(titulos: list, ruta: str):
    """Guarda los títulos de noticias en un archivo de texto."""
    try:
        crear_archivo(ruta)
        with open(os.path.join(ruta, "noticias.txt"), "w", encoding="utf-8") as file:
            for titulo in titulos:
                file.write(titulo + "\n")
    except Exception as e:
        print(f"Error al guardar las noticias: {e}")


def limpiar_archivos(ruta: str):
    """Limpia los archivos en la ruta especificada."""
    try:
        if os.path.exists(ruta):
            shutil.rmtree(ruta)
        os.makedirs(ruta)
    except Exception as e:
        print(f"Error al limpiar los archivos: {e}")


def realizar_scraping():
    """Función principal para realizar el web scraper."""
    try:
        limpiar_archivos(RUTA_ARCHIVO)
        print("Obteniendo noticias...")
        titulos = obtener_noticias(URL)
        if not titulos:
            print("No se encontraron noticias.")
            return
        print(f"Se encontraron {len(titulos)} noticias.")
        print("Guardando noticias...")
        guardar_noticias(titulos, RUTA_ARCHIVO)
        print(f"Se han guardado {len(titulos)} noticias en {RUTA_ARCHIVO} noticias.txt")
    except Exception as e:
        print(f"Error en el proceso del scraping: {e}")


realizar_scraping()
