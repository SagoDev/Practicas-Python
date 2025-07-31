import random

historial = {}
registros_dado_a = []
registros_dado_b = []


def tirar_dado():
    """Simula la tirada de un dado y devuelve un int."""
    return random.randint(1, 6)


def comparar_dados(a: int, b: int):
    """Compara si dos resultados son iguales y devuelve un bool"""
    return a == b


def listar_historial():
    """Lista todas las tiradas realizadas."""
    if len(historial.items()) == 0:
        print("\n No hay resultados. \n")

    for registro, valores in historial.items():
        print(f"Tirada {registro}: {valores[0], valores[1]}")


def agregar_al_historial(a: int, b: int):
    """Agrega el resultado de la tirada al historial."""
    tirada = {(len(historial.items()) + 1): [a, b]}
    historial.update(tirada)

    registros_dado_a.append(a)
    registros_dado_b.append(b)


def verificar_respuesta(respuesta: str):
    """Control de flujo. Recibe un str, lo válida y devuelve un bool o None"""
    if respuesta not in ("SI", "NO"):
        return None
    if respuesta == "NO":
        return False

    return True


def contar_ocurrencias(valores: list[int]):
    """Cuenta las ocurrencias de valores de una list y devuelve un dict con las ocurrencias."""
    reporte_ocurrencias = []
    valores_unicos = []

    for valor in valores:
        if valor not in valores_unicos:
            ocurrencias = [valor, valores.count(valor)]
            reporte_ocurrencias.append(ocurrencias)
            valores_unicos.append(valor)

    return reporte_ocurrencias


def contar_dobles():
    """Cuenta la cantidad de dobles conseguidos."""
    total_dobles = 0

    for _, valores in historial.items():
        if valores[0] == valores[1]:
            total_dobles += 1

    return total_dobles


def listar_ocurrencias(dado: str):
    """Lista los valores y sus ocurrencias respecto a las tiradas de un dado."""

    if dado == "A":
        ocurrencias_dado = contar_ocurrencias(registros_dado_a)

    if dado == "B":
        ocurrencias_dado = contar_ocurrencias(registros_dado_b)

    print("Valor | Ocurrencias")
    print(" ---  |     ---")

    for registro in ocurrencias_dado:
        print(f"  {registro[0]}   |      {registro[1]}")


def encontrar_mayor_ocurrencia(letra: str):
    """Encuentra el valor de mayor ocurrencia en los registros."""
    mayor = 0

    if letra == "A":
        registros = contar_ocurrencias(registros_dado_a)

    if letra == "B":
        registros = contar_ocurrencias(registros_dado_b)

    for registro in registros:
        if registro[1] > mayor:
            mayor = registro[1]

    if mayor == 1:
        print("No hay valores repetidos. \n")
    else:
        print("\n Valores con más ocurrencias: \n")
        for registro in registros:
            if registro[1] == mayor:
                print(f"Valor {registro[0]} con {registro[1]} ocurrencias.")


def realizar_analisis():
    """Realiza un análisis a partir de los datos del historial."""

    print("\n ------ Análisis de tiradas ------ \n")
    print(f"- Tiradas realizadas: {len(historial.items())} \n")
    print(f"- Dobles conseguidos: {contar_dobles()} \n")

    print("- Ocurrencias en Dado A: \n")
    listar_ocurrencias("A")
    encontrar_mayor_ocurrencia("A")

    print("\n- Ocurrencias en Dado B: \n")
    listar_ocurrencias("B")
    encontrar_mayor_ocurrencia("B")


while True:
    print("\n ------ Simulador de Dados ------ \n")

    print("1- Tirar dados!")
    print("2- Ver historial")
    print("3- Cerrar")

    opcion = input("\n ¿Qué desea hacer?: ")

    if opcion == "1":

        dado_a = tirar_dado()
        dado_b = tirar_dado()

        print("\n ------Tirar Dados ------ \n")
        print(f"Lanzando primer dado... Su valor es {dado_a}!")
        print(f"Lanzando segundo dado... Su valor es {dado_b}!\n")

        if comparar_dados(dado_a, dado_b):
            print("Ha salido un doble! Felicitaciones!\n")
        else:
            print("No es doble. Suerte la proxima!\n")

        agregar_al_historial(dado_a, dado_b)

    if opcion == "2":
        print("\n ------ Historial de Resultados ------ \n")
        listar_historial()

        if len(historial.items()) > 0:
            while True:
                analizar = input("\n ¿Desea ver un análisis?(SI/NO): ").upper()
                res = verificar_respuesta(analizar)
                if res is None:
                    print("\n Por favor responda SI o NO.")
                elif res:
                    realizar_analisis()
                    break
                else:
                    break

    if opcion == "3":
        print("\n Gracias por usar el simulador. Hasta la proxima!")
        break

    if opcion not in ("1", "2", "3"):
        print("\n Responda con una opción válida.")
