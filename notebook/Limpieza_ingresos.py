import pandas as pd

def limpiar_datos(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    if data_frame_limpio.empty:
        return data_frame_limpio


    if 'mcliente' in data_frame_limpio.columns:
        def extraer_id(val):
            if isinstance(val, dict) and 'id' in val:
                return val['id']
            return val
        # Convertimos la columna de un objeto dict a un número ID plano
        data_frame_limpio['mcliente'] = data_frame_limpio['mcliente'].apply(extraer_id)

    # 1. Limpiar las columnas string del data frame
    valores_validos_categoria = ["intereses", "comisiones", "ventas", "creditos"]
    
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].astype(str).str.strip()
    data_frame_limpio["categoria"] = data_frame_limpio["categoria"].astype(str).str.strip().str.lower()
    
    data_frame_limpio["categoria"] = data_frame_limpio["categoria"].where(
        data_frame_limpio["categoria"].isin(valores_validos_categoria), "otros"
    )

    # 2. Limpiar las columnas numéricas y de fecha del data frame
    data_frame_limpio["valor"] = pd.to_numeric(data_frame_limpio["valor"], errors="coerce")
    data_frame_limpio["fecha"] = pd.to_datetime(data_frame_limpio["fecha"], errors="coerce")
    
    if "createdAt" in data_frame_limpio.columns:
        data_frame_limpio["createdAt"] = pd.to_datetime(data_frame_limpio["createdAt"], errors="coerce")

    # 2.1 Limpiando campos numéricos que no tengan valores válidos
    data_frame_limpio = data_frame_limpio[data_frame_limpio["valor"] > 0]

    # 3. Limpiar columnas obligatorias vacías
    data_frame_limpio["descripcion"] = data_frame_limpio["descripcion"].replace(r'^\s*$', pd.NA, regex=True)

    # 4. Eliminar registros que tengan datos obligatorios vacíos
    columnas_obligatorias = ["fecha", "valor", "descripcion", "categoria"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    # =========================================================================
    # 5. Eliminar registros duplicados (Ahora sí funcionará perfectamente)
    # =========================================================================
    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio