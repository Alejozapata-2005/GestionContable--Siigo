import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1 limpiar las columnas string del data frame
    valores_validos_categoria = ["intereses", "comisiones", "ventas", "creditos"]
    
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].astype(str).str.strip()
    data_frame_limpio["categoria"] = data_frame_limpio["categoria"].astype(str).str.strip().str.lower()
    data_frame_limpio["categoria"] = data_frame_limpio["categoria"].where(
        data_frame_limpio["categoria"].isin(valores_validos_categoria), pd.NA
    )

    # 2 limpiar las columnas numericas (y de fecha) del data frame
    data_frame_limpio["valor"] = pd.to_numeric(data_frame_limpio["valor"], errors="coerce")
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors="coerce")

    # 2.1 limpiando campos numericos que no tengan valores validos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["valor"] > 0]

    # 3 limpiar columnas obligatorias
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].replace("", pd.NA)

    # 4 eliminar registros que tengan datos obligatorios vacios
    columnas_obligatorias = ["fecha", "valor", "descripcion", "categoria"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # 5 eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio