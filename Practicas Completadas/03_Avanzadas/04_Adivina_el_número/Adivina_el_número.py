import random


def adivina_el_numero():
    """Juego para adivinar un número entre 1 y 100."""
    print("¡Bienvenido al juego 'Adivina el número'!")
    print("\n ----------------------- \n")
    print("Estoy pensando en un número entre 1 y 100. \n")

    numero = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if adivinanza < numero:
                print("Demasiado bajo. Intenta de nuevo.")
            elif adivinanza > numero:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(
                    f"¡Felicidades! Has adivinado el número {numero} en {intentos} intentos."
                )
                break
        except ValueError:
            print("Por favor, introduce un número válido.")


adivina_el_numero()
