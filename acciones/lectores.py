import pandas as pd

def lector_existe(dni: str):
    try:
        df = pd.read_csv("csv/lectores.csv")
        return dni in df["dni"].astype(str).values
    except FileNotFoundError:
        return False

def registrar_lector(dni: str, nombre: str):
    df = pd.DataFrame([[dni, nombre]], columns=["dni", "nombre"])
    df.to_csv("csv/lectores.csv", mode="a", header=False, index=False)

def tiene_prestamo_pendiente(dni:str) -> bool:
    try:
        df = pd.read_csv("csv/prestamos.csv")
        prestamos_pendientes = df [(df["dni"].astype(str) == dni) & (df["devuelto"] == 0)]
        
        if not prestamos_pendientes.empty:
            print(f"El lector con DNI {dni} tiene {len(prestamos_pendientes)} préstamo(s) pendiente(s).")
            return True
        else:
            print(f"El lector con DNI {dni} no tiene préstamos pendientes.")
            return False
    except FileNotFoundError:
        print("El archivo de préstamos no fue encontrado.")
        return False
