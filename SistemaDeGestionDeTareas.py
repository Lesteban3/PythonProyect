class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = "pendiente"  # Estado inicial de la tarea

    def __str__(self):
        return f"Título: {self.titulo}, Descripción: {self.descripcion}, Estado: {self.estado}"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        print(f"Tarea '{titulo}' agregada.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            print("Lista de tareas:")
            for tarea in self.tareas:
                print(tarea)

    def buscar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                print(f"Tarea encontrada: {tarea}")
                return tarea
        print("Tarea no encontrada.")
        return None

    def actualizar_estado_tarea(self, titulo):
        tarea = self.buscar_tarea(titulo)
        if tarea:
            tarea.estado = "completada"
            print(f"Estado de '{titulo}' actualizado a 'completada'.")

    def eliminar_tarea(self, titulo):
        tarea = self.buscar_tarea(titulo)
        if tarea:
            self.tareas.remove(tarea)
            print(f"Tarea '{titulo}' eliminada.")
        else:
            print("No se pudo eliminar la tarea, no encontrada.")

    def menu(self):
        while True:
            print("\n--- Gestor de Tareas ---")
            print("1. Agregar tarea")
            print("2. Mostrar tareas")
            print("3. Buscar tarea")
            print("4. Actualizar estado de tarea")
            print("5. Eliminar tarea")
            print("6. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                titulo = input("Título de la tarea: ")
                descripcion = input("Descripción: ")
                self.agregar_tarea(titulo, descripcion)
            elif opcion == "2":
                self.mostrar_tareas()
            elif opcion == "3":
                titulo = input("Título de la tarea a buscar: ")
                self.buscar_tarea(titulo)
            elif opcion == "4":
                titulo = input("Título de la tarea a actualizar: ")
                self.actualizar_estado_tarea(titulo)
            elif opcion == "5":
                titulo = input("Título de la tarea a eliminar: ")
                self.eliminar_tarea(titulo)
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")


gestor = GestorTareas()
gestor.menu()
