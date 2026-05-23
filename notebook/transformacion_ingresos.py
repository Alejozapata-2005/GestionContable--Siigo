import pandas as pd

def transformar_datos_ingresos(data_frame_limpio_ingresos):
    # Hacemos una copia para no alterar el DataFrame original por fuera
    df = data_frame_limpio_ingresos.copy()

    # 1. ADAPTACIÓN DE LA COLUMNA DE FECHA DE CREACIÓN
    if 'createdAt' in df.columns:
        df = df.rename(columns={'createdAt': 'created_at'})
        
    # 2. ASIGNACIÓN DEL CLIENTE_ID
    # Como 'Limpieza_ingresos' ya aplanó 'mcliente' convirtiéndolo en un ID numérico,
    # aquí solo renombramos la columna para que el resto de las agrupaciones funcionen.
    if 'mcliente' in df.columns:
        df = df.rename(columns={'mcliente': 'cliente_id'})
    elif 'clienteId' in df.columns:
        df = df.rename(columns={'clienteId': 'cliente_id'})
    elif 'cliente_id' not in df.columns:
        # Salvavidas en caso de que no existiera ninguna referencia
        df['cliente_id'] = df['id']

 # --- NORMALIZACIÓN CRÍTICA ---
    # Salvavidas en caso de que 'fecha' no venga textualmente así desde la API/limpieza
    if 'fecha' not in df.columns:
        if 'date' in df.columns:
            df = df.rename(columns={'date': 'fecha'})
        elif 'created_at' in df.columns:
            df['fecha'] = df['created_at']
        else:
            # Crea la columna vacía si no existe ninguna referencia temporal para evitar que el script muera
            df['fecha'] = pd.NaT

    # Convertimos las fechas de forma segura manejando errores
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce').dt.date
    
    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce').dt.date
    else:
        df['created_at'] = df['fecha']


    # --- 5 TRANSFORMACIONES ACTUALIZADAS ---

    # 1. TOTAL DE INGRESOS POR CATEGORÍA
    agrupacion1 = df.groupby("categoria")["valor"].sum().reset_index(name="total_ingresos")

    # 2. CONTEO DE TRANSACCIONES DE ALTO VALOR POR CATEGORÍA
    filtro2 = df.query("valor >= 500000")
    if filtro2.empty: 
        filtro2 = df
    agrupacion2 = filtro2.groupby("categoria")["cliente_id"].count().reset_index(name="conteo_transacciones_altas")

    # 3. PROMEDIO DE INGRESOS POR FECHA DE CREACIÓN
    agrupacion3 = df.groupby("created_at")["valor"].mean().reset_index(name="promedio_diario")

    # 4. RENDIMIENTO DE LA CATEGORÍA PRINCIPAL ("VENTAS")
    filtro4 = df.query("categoria == 'ventas'")
    agrupacion4 = filtro4.groupby("fecha")["valor"].sum().reset_index(name="total_ventas_diarias")

    # 5. MONTO MÍNIMO Y MÁXIMO REGISTRADO POR CLIENTE
    agrupacion5 = df.groupby("cliente_id")["valor"].agg(["min", "max"]).reset_index()
    agrupacion5.columns = ["cliente_id", "monto_minimo", "monto_maximo"]


    # Resumen de las agrupaciones para el retorno
    agrupacion_resumen = {
        "ingresos_por_categoria": agrupacion1,
        "conteo_altos_ingresos": agrupacion2,
        "promedio_temporal": agrupacion3,
        "ventas_diarias": agrupacion4,
        "auditoria_cliente": agrupacion5
    }

    return agrupacion_resumen