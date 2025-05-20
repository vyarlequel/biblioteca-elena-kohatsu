from menus.menu_libros_mas_prestados import mostrar_menu_libros_mas_prestados
from menus.menu_registrar_solicitud import menu_registrar_solicitud
from utils.consola import limpiar_pantalla
from acciones.lectores import tiene_prestamo_pendiente

def menu_principal():
    limpiar_pantalla()

    while True:
        print("=== Biblioteca Elena Kohatsu ===")
        print("1. Registrar préstamo de un libro")
        print("2. Reporte de libros más prestados")
        print("3. Verificar si lector tiene préstamos pendientes")
        print("4. Reporte de libros que no han sido devueltos")
        print("5. Salir")
        print("\n")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_registrar_solicitud()
        elif opcion == "2":
            mostrar_menu_libros_mas_prestados()
        elif opcion == "3":
            dni = input("Ingrese el DNI del lector: ")
            tiene_prestamo_pendiente(dni)
        elif opcion == "4":
            pass
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

        limpiar_pantalla()
