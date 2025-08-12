class contacto:

    def __init__(self, nombre: str, telefono: str) -> None:
        self.nombre = nombre
        self.telefono = telefono


class agenda:

    def __init__(self) -> None:
        self.contactos = {}

    def listar_contactos(self):
        """Lista todos los contactos registrados en la agenda."""

        try:
            contactos = self.contactos.items()
            if len(contactos) == 0:
                print("No hay contactos registrados.")

            for indice, contacto in contactos:
                print(f"{indice} - {contacto.nombre}: {contacto.telefono}")
        except Exception as e:
            print(f"\n Error listar contactos: {e} \n")
            return

    def ver_info_contacto(self):
        """Despliega la información de un contacto."""

        try:
            indice = int(input("\n Ingrese indice del contacto: "))
            contacto = self.contactos.get(indice)

            print("\n ------ Info del Contacto ------ \n")
            print(f"Nombre: {contacto.nombre} \n")
            print(f"Telefono: {contacto.telefono} \n")

            print("1- Eliminar contacto")
            print("2- Modificar contacto")
            print("3- Regresar")
            while True:
                opcion = int(input("\n ¿Qué desea hacer?: "))

                if opcion == 1:
                    self.eliminar_contacto(indice)
                elif opcion == 2:
                    self.modificar_contacto(indice)
                elif opcion == 3:
                    break
                else:
                    print("\n Eliga una opción válida.")
        except Exception as e:
            print(f"\n Error al ver info de contacto: {e} \n")
            return

    def agregar_contacto(self):
        """Agrega un contacto a la agenda."""
        try:
            print("\n ------ Agregar Nuevo Contacto ------ \n")

            contacto_nombre = input("Nombre del contacto: ")
            contacto_telefono = input("Télefono del contacto: ")

            indice = len(self.contactos.items()) + 1
            nuevo_contacto = {indice: contacto(contacto_nombre, contacto_telefono)}

            self.contactos.update(nuevo_contacto)
            print("\n Contacto agregado con éxito. \n")
        except Exception as e:
            print(f"\n Error al agregar contacto: {e} \n")
            return

    def eliminar_contacto(self, indice: int):
        """Elimina un contacto a la agenda."""
        try:
            contactos = self.contactos
            contactos.pop(indice)
            print("\n Contacto eliminado con éxito. \n")
        except Exception as e:
            print(f"\n Error al eliminar contacto: {e} \n")
            return

    def modificar_contacto(self, indice: int):
        """Modifica nombre o  un contacto."""
        try:
            contacto = self.contactos.get(indice)
            print("\n1- Modificar nombre")
            print("2- Modificar número")
            print("3- Regresar")
            while True:

                modificar = int(input("\n ¿Qué desea hacer?: "))

                if modificar == 1:
                    nuevo_nombre = input("\n Ingrese nuevo nombre: ")
                    contacto.nombre = nuevo_nombre
                    print("\n Nombre modificado con éxito. \n")

                elif modificar == 2:
                    nuevo_telefono = int(input("\n Ingrese nuevo teléfono: "))
                    contacto.telefono = nuevo_telefono
                    print("\n Número modificado con éxito. \n")

                elif modificar == 3:
                    break

                else:
                    print("\n Eliga una opción válida.")
            return
        except Exception as e:
            print(f"\n Error al modificar contacto: {e} \n")
            return


mi_agenda = agenda()

while True:

    print("\n ------ Agenda de Contactos ------ \n")
    mi_agenda.listar_contactos()
    cantidad_contactos = len(mi_agenda.contactos.items())
    print("\n ----------------------- \n")

    if cantidad_contactos == 0:
        print("1- Agregar un contacto")
        print("3- Cerrar")
    else:
        print("1- Agregar un contacto")
        print("2- Ver Info de contacto")
        print("3- Cerrar")

    while True:
        accion = int(input("\n ¿Qué desea hacer?: "))

        if accion == 1:
            mi_agenda.agregar_contacto()
            break

        elif accion == 2 and cantidad_contactos != 0:
            mi_agenda.ver_info_contacto()
            break

        elif accion == 3:
            print("\n Gracias por usar la agenda. Hasta la proxima!")
            print("\n ----------------------- \n")
            break
        else:
            print("\n Eliga una opción válida.")
