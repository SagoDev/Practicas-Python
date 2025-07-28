contactos = {
    "juan": "123",
    "lucia": "456",
    "santiago": "789",
}


def agregar_contacto(nombre: str, telefono: str):
    """Agrega un nuevo contacto a la agenda."""
    contacto = {nombre: telefono}
    contactos.update(contacto)
    return True


def listar_contactos():
    """Lista todos los contactos registrados en la agenda."""
    if len(contactos.items()) == 0:
        print("\n No hay contactos agendados. \n")

    for nombre, telefono in contactos.items():
        print(f"{nombre} : {telefono}")


def regresar(respuesta: str):
    """Control de flujo. Recibe un str, lo válida y devuelve un bool o None"""
    if respuesta != "SI" and respuesta != "NO":
        return None
    elif respuesta == "NO":
        return False
    else:
        return True


while True:
    print("\n ------ Agenda de Contactos ------ \n")
    print("------ ¿Qué desea hacer? ------ \n")

    print("1- Ver Agenda")
    print("2- Agregar un contacto")
    print("3- Cerrar")

    opcion = input("\n Opción: ")

    if opcion == "1":
        print(" ------ Contactos ------ \n")
        listar_contactos()
        print(" ----------------------- \n")
        while True:
            res = regresar(input("Regresar(SI/NO): ").upper())

            if res is None:
                print("\n Por favor responda SI o NO. \n")
            elif not res:
                print(f"{res}")
                opcion = "3"
                break
            else:
                break

    if opcion == "2":
        print("\n ------ Agregar Nuevo Contacto ------ \n")
        contacto_nombre = input("Nombre del contacto: ")
        contacto_telefono = input("Télefono del contacto: ")
        if agregar_contacto(contacto_nombre, contacto_telefono):
            print("\n Contacto agregado con éxito \n")
        else:
            print("\n No se pudo agregar el contacto. \n")

    if opcion == "3":
        print("\n Gracias por usar la agenda. Hasta la proxima!")
        print("\n ----------------------- \n")
        break
