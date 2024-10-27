class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"


class AgendaContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono):
        contacto = Contacto(nombre, telefono)
        self.contactos.append(contacto)
        print(f"Contacto '{nombre}' agregado.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Contacto encontrado: {contacto}")
                return contacto
        print("Contacto no encontrado.")
        return None

    def eliminar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.contactos.remove(contacto)
            print(f"Contacto '{nombre}' eliminado.")
        else:
            print("No se pudo eliminar el contacto, no encontrado.")

    def menu(self):
        while True:
            print("\n--- Agenda de Contactos ---")
            print("1. Agregar contacto")
            print("2. Mostrar contactos")
            print("3. Buscar contacto")
            print("4. Eliminar contacto")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                self.agregar_contacto(nombre, telefono)
            elif opcion == "2":
                self.mostrar_contactos()
            elif opcion == "3":
                nombre = input("Nombre del contacto a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == "4":
                nombre = input("Nombre del contacto a eliminar: ")
                self.eliminar_contacto(nombre)
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")



agenda = AgendaContactos()
agenda.menu()
