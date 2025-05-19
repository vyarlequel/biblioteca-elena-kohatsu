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
