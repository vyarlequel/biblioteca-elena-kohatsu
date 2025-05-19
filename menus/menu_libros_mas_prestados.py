from utils.consola import limpiar_pantalla
from acciones.reportes import obtener_libros_mas_prestados

def mostrar_menu_libros_mas_prestados():
    limpiar_pantalla()

    print("Libros más prestados:\n")
    resultado = obtener_libros_mas_prestados()

    if not resultado:
        print("No hay préstamos registrados.")
    else:
        print("{:<45}{}".format("Titulo", "Cantidad"))
        print("-" * 53)

        for codigo, cantidad in resultado:
            print("{:<45}{}".format(codigo, cantidad))

    input("\nPresione cualquier tecla para volver...")