def analizar_texto(archivo: str):

    with open(
        archivo,
        "r",
    ) as a:
        contenido = a.read()
        palabras = len(contenido.split(" "))
        lineas = len(contenido.splitlines())

        return f"El texto contiene {lineas} lineas y {palabras} palabras"


print(analizar_texto("Practicas Completadas/02_Intermedio/material/texto_01.txt"))
