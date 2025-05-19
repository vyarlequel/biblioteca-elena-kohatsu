from utils.consola import limpiar_pantalla
from acciones.lectores import lector_existe, registrar_lector

def menu_registrar_solicitud():
    limpiar_pantalla()

    print("Registrar solicitud de préstamo")

    dni = input("\nIngrese DNI del lector: ")

    if not lector_existe(dni):
        nombre = input("Ingrese nombre y apellidos: ")
        registrar_lector(dni, nombre)

    # Debe verificar si tiene un préstamo pendiente
    print("Verificar si el lector tiene un préstamo pendiente")

    # Mostrar formulario de registro de solicitud
    print("Mostrar formulario de registro de solicitud y registrar")