import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def cargar_datos(ruta):
    """
    Carga un archivo CSV y devuelve un DataFrame.
    """
    try:
        df = pd.read_csv(ruta)
        print(f"Datos cargados correctamente: {df.shape[0]} filas, {df.shape[1]} columnas.")
        return df
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None

def mostrar_info_basica(df):
    """
    Muestra info básica: estructura y estadísticas del DataFrame.
    """
    print(df.info())
    print("\nResumen estadístico:\n", df.describe())

def graficar_ventas_por_categoria(df, columna_categoria, columna_ventas):
    """
    Gráfico interactivo con Plotly de ventas por categoría.
    """
    fig = px.bar(df.groupby(columna_categoria)[columna_ventas].sum().reset_index(),
                 x=columna_categoria, y=columna_ventas,
                 title=f"Ventas por {columna_categoria}")
    fig.show()

