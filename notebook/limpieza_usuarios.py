import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    if data_frame_limpio.empty:
        return data_frame_limpio

    # 1. Pasamos las columnas existentes a minúsculas para unificar
    data_frame_limpio.columns = data_frame_limpio.columns.str.lower()

    # 2. Mapeamos sinónimos exactos del backend
    mapeo_auxiliar = {
        'nombreusuario': 'nombre',
        'name': 'nombre',
        'correo': 'correo',
        'email': 'correo',
        'rol': 'rol',
        'role': 'rol'
    }
    data_frame_limpio = data_frame_limpio.rename(columns=mapeo_auxiliar)

    # =========================================================================
    # ELIMINAR COLUMNAS PROBLEMÁTICAS (Evita el TypeError: unhashable dict)
    # En lugar de convertir a str, eliminamos las columnas de relaciones que NO 
    # usamos en analítica de usuarios para que drop_duplicates corra limpio.
    # =========================================================================
    columnas_validas = ['id', 'nombre', 'correo', 'rol', 'created_at', 'createdat']
    columnas_a_borrar = [col for col in data_frame_limpio.columns if col not in columnas_validas]
    data_frame_limpio = data_frame_limpio.drop(columns=columnas_a_borrar, errors='ignore')

    # Aseguramos la existencia física de las columnas clave
    columnas_requeridas = ["nombre", "rol", "correo"]
    for col in columnas_requeridas:
        if col not in data_frame_limpio.columns:
            data_frame_limpio[col] = pd.NA

    # 3. Reemplazar nulos de texto iniciales
    for columna in columnas_requeridas:
        data_frame_limpio[columna] = data_frame_limpio[columna].replace(
            [None, "None", "nan", "NaN"], pd.NA
        )

    # 4. Procesamiento y estandarización real de los datos
    data_frame_limpio["nombre"] = (
        data_frame_limpio["nombre"].fillna("Sin Nombre").astype(str).str.strip().str.title()
    )
    
    data_frame_limpio["rol"] = (
        data_frame_limpio["rol"].fillna("contador").astype(str).str.strip().str.lower()
    )
    data_frame_limpio["rol"] = data_frame_limpio["rol"].replace({"usuarios": "contador", "usuario": "contador"})
    
    data_frame_limpio["correo"] = (
        data_frame_limpio["correo"].fillna("sin_correo@gestion.com").astype(str).str.strip().str.lower()
    )

    # 5. Limpiar las columnas numéricas
    if "id" in data_frame_limpio.columns:
        data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    else:
        data_frame_limpio["id"] = range(1, len(data_frame_limpio) + 1)

    # 6. Filtrar IDs válidos y eliminar nulos reales (Quitamos el borrado de 'Sin Nombre')
    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    
    # Eliminamos solo si el correo o el ID están verdaderamente vacíos en el origen
    data_frame_limpio = data_frame_limpio.dropna(subset=["id", "correo"])

    # 7. Eliminar registros duplicados (Sin columnas extrañas, irá súper rápido)
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio