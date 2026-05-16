import pandas as pd


def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #1 limpiar las columnas string del data frame
    valores_validos_rol = ["contador"]
    columnas_texto = ["nombre", "rol", "correo"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].replace(
            [None, "None", "nan", "NaN"], pd.NA
        )

    data_frame_limpio["nombre"] = (
        data_frame_limpio["nombre"].astype("string").str.strip().str.title()
    )
    data_frame_limpio["rol"] = (
        data_frame_limpio["rol"].astype("string").str.strip().str.lower()
    )
    data_frame_limpio["rol"] = data_frame_limpio["rol"].replace(
        {"usuarios": "contador"}
    )
    data_frame_limpio["correo"] = (
        data_frame_limpio["correo"].astype("string").str.strip().str.lower()
    )
    data_frame_limpio["rol"] = data_frame_limpio["rol"].where(
        data_frame_limpio["rol"].isin(valores_validos_rol), pd.NA
    )

    #2 limpiar las columnas numericas del data frame
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")

    #2.1 limpiando campos numericos que no tengan valores validos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]

    #3 limpiar columnas obligatorias
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].replace("", pd.NA)
    data_frame_limpio["correo"] = data_frame_limpio["correo"].replace("", pd.NA)

    #4 eliminar registros que tengan datos obligatorios vacios
    columnas_obligatorias = ["id", "nombre", "rol", "correo"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    #5 eliminar registros duplicados
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio
