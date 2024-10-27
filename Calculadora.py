def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mult(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def mostrar_menu():
    print("\nCalculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo del programa.")
        break

    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {mult(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción no válida, intenta de nuevo.")
