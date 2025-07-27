def obtener_numeros_primos(num: int):
    """Recibe una lista de números y devuelve los números primos en ella."""
    if num < 2:
        return "No hay números primos en la lista."

    lista_de_numeros = set(range(2, num + 1))
    divisores_primos = (2, 3, 5, 7)
    numeros_primos = []

    for numero in lista_de_numeros:
        if (
            numero in divisores_primos
            or numero % 2 != 0
            and numero % 3 != 0
            and numero % 5 != 0
            and numero % 7 != 0
        ):
            numeros_primos.append(numero)

    return numeros_primos


print("----- Números Primos -----\n")
print("Ingrese un número y obtendrá los números primos hasta ese número.\n")

numero_ingresado = int(input("Número: "))

print(
    f"\n Lista de numeros primos hasta el numero {numero_ingresado}: {obtener_numeros_primos(numero_ingresado)}\n"
)
