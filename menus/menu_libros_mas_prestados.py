from menus.menu_users import user_menu
from menus.menu_reports import report_menu
from menus.menu_settings import settings_menu

def main_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Usuarios")
        print("2. Reportes")
        print("3. Configuración")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            user_menu()
        elif opcion == "2":
            report_menu()
        elif opcion == "3":
            settings_menu()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
