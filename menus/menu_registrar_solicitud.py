from utils.consola import limpiar_pantalla
from acciones.lectores import lector_existe, registrar_lector, tiene_prestamo_pendiente

def mostrar_menu_registrar_solicitud():
    limpiar_pantalla()

    print("Registrar solicitud de préstamo")

    dni = input("\nIngrese DNI del lector: ")

    if not lector_existe(dni):
        nombre = input("Ingrese nombre y apellidos: ")
        registrar_lector(dni, nombre)

    if tiene_prestamo_pendiente(dni):
        input("\nPresione cualquier tecla para volver...")
        return

    # Mostrar formulario de registro de solicitud
    print("Mostrar formulario de registro de solicitud y registrar")