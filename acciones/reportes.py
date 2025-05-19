import pandas as pd

def obtener_libros_mas_prestados():
    try:
        prestamos = pd.read_csv("csv/prestamos.csv")
        libros = pd.read_csv("csv/libros.csv")

        if prestamos.empty and libros.empty:
            return []

        df_prestamos = prestamos["codigo_libro"].value_counts().reset_index()
        df_prestamos.columns = ["codigo_libro", "cantidad_prestamos"]
        df_prestamos = df_prestamos.merge(libros, left_on="codigo_libro", right_on="codigo")
        df_prestamos = df_prestamos[["titulo", "cantidad_prestamos"]]
        df_prestamos = df_prestamos.sort_values(by="cantidad_prestamos", ascending=False)

        return df_prestamos.values.tolist()
    except FileNotFoundError:
        return "Archivo no encontrado"
    except Exception as e:
        return f"Error: {e}"
    
def obtener_libros_sin_devolver():
    pass