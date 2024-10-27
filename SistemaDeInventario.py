class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        try:
            cantidad = int(cantidad)
            precio = float(precio)
            producto = Producto(nombre, cantidad, precio)
            self.productos.append(producto)
            print(f"Producto '{nombre}' agregado al inventario.")
        except ValueError:
            print("Error: Cantidad o precio inválidos. Intente de nuevo.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Lista de productos:")
            for producto in self.productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"Producto encontrado: {producto}")
                return producto
        print("Producto no encontrado.")
        return None

    def actualizar_cantidad(self, nombre, nueva_cantidad):
        producto = self.buscar_producto(nombre)
        if producto:
            try:
                nueva_cantidad = int(nueva_cantidad)
                producto.cantidad = nueva_cantidad
                print(f"Cantidad de '{nombre}' actualizada a {nueva_cantidad}.")
            except ValueError:
                print("Error: Cantidad inválida. Intente de nuevo.")

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print("No se pudo eliminar el producto, no encontrado.")

    def menu(self):
        while True:
            print("\n--- Sistema de Inventario ---")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Buscar producto")
            print("4. Actualizar cantidad de producto")
            print("5. Eliminar producto")
            print("6. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre del producto: ")
                cantidad = input("Cantidad: ")
                precio = input("Precio: ")
                self.agregar_producto(nombre, cantidad, precio)
            elif opcion == "2":
                self.mostrar_productos()
            elif opcion == "3":
                nombre = input("Nombre del producto a buscar: ")
                self.buscar_producto(nombre)
            elif opcion == "4":
                nombre = input("Nombre del producto a actualizar: ")
                nueva_cantidad = input("Nueva cantidad: ")
                self.actualizar_cantidad(nombre, nueva_cantidad)
            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ")
                self.eliminar_producto(nombre)
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")



inventario = Inventario()
inventario.menu()
