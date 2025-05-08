def menu_principal():
    while True:
        print("\n=== Biblioteca Elena Kohatsu ===")
        print("1. Registrar préstamo de un libro")
        print("2. Reporte de libros más prestados")
        print("3. Salir")
        print("\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Opcion 1")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")