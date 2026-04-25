import pandas as pd


def describir_datos(data_frame_limpio):
    print("Descripcion del data set")
    print(f"Numero de filas del dataset: {data_frame_limpio.shape[0]}")
    print(f"numero de columnas del dataset: {data_frame_limpio.shape[1]}")
    print(f"lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f" tipos de datos de cada atributo: {data_frame_limpio.dtypes}")

    #estadisticas(solo aplica para datos numericos)
    print("*estadisticas*")
    print(f"{data_frame_limpio['id'].describe()}")

    #informacion de conteos valiosos
    print("*conteos*")
    print(f"{data_frame_limpio['nombre'].value_counts()}")
    print(f"{data_frame_limpio['rol'].value_counts()}")
    print(f"{data_frame_limpio['correo'].value_counts()}")




