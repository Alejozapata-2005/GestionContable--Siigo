## toda rutina de analisis debe describir el data set
#1. es importante conocer cuantos registros tengo
#2. Es importante  conocer cuantos atributos tengo 
#3. Es util tener acceso a una lista con los nombres de los atributos
#4. es util hacer conteo de algunas columnas de interes 
#5. Es util conocer las estadisticas descriptivas de los campos numericos
#Media-max-min-std-percentiles
#Si tengo fechas es util conocer cual es la fecha mas antigua y la mas actual

import pandas as pd


def describir_datos(data_frame_limpio):
    print("*** Descripcion del data set ***")
    print(f"Numero de filas del data set: {data_frame_limpio.shape[0]}")
    print(f"Numero de columnas del data set: {data_frame_limpio.shape[1]}")
    print(f"Lista de columnas disponibles: {list(data_frame_limpio.columns)}")
    print(f"Tipos de dato de cada atributo:\n{data_frame_limpio.dtypes}")

    ## Estadisticas (solo aplica para datos numericos)
    print("\n*** Estadisticas ***")
    print(f"{data_frame_limpio[['id', 'valor']].describe()}")

    ## Informacion de conteos valiosos 
    print("\n*** Conteos ***")
    print(f"{data_frame_limpio['categoria'].value_counts()}")
    print(f"{data_frame_limpio['descripcion'].value_counts()}")

    # Describiendo las fechas 
    print("\n*** Descripcion de fechas ***")
    print(f"Fecha mínima: {data_frame_limpio['fecha'].min()}")
    print(f"Fecha máxima: {data_frame_limpio['fecha'].max()}")