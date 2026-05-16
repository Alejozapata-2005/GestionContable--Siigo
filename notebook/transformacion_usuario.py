import pandas as pd

def transformar_datos(data_frame_limpio):
    df = data_frame_limpio.copy()

    # 1. Columna auxiliar para analizar el proveedor del correo.
    # Convertimos a minúsculas para que el cruce sea 100% exacto
    df["dominio"] = df["correo"].str.split("@").str[-1].str.lower().str.strip()
    
    # CORRECCIÓN CRÍTICA: Cambiamos 'empresa.com' por 'gestion.com' que es tu dominio real
    df["tipo_correo"] = df["dominio"].eq("gestion.com").map(
        {True: "corporativo", False: "no_corporativo"}
    )

    # transformacion 1 (usuarios por dominio de correo)
    filtro1 = df
    agrupacion1 = (
        filtro1.groupby("dominio")["id"]
        .count()
        .reset_index(name="conteo")
        .sort_values("conteo", ascending=False)
    )

    # transformacion 2 (usuarios por nombre)
    filtro2 = df
    agrupacion2 = (
        filtro2.groupby("nombre")["id"]
        .count()
        .reset_index(name="conteo")
        .sort_values("conteo", ascending=False)
    )

    # transformacion 3 (usuarios por tipo de correo)
    filtro3 = df
    agrupacion3 = (
        filtro3.groupby("tipo_correo")["id"]
        .count()
        .reset_index(name="conteo")
        .sort_values("conteo", ascending=False)
    )

    # transformacion 4 (usuarios por nombre dentro de cada dominio)
    filtro4 = df
    agrupacion4 = (
        filtro4.groupby(["dominio", "nombre"])["id"]
        .count()
        .reset_index(name="conteo")
        .sort_values(["dominio", "conteo"], ascending=[True, False])
    )

    # transformacion 5 (usuarios corporativos por nombre)
    # ¡Ahora sí se llenará porque ya existen usuarios con 'corporativo'!
    filtro5 = df[df["tipo_correo"] == "corporativo"]
    agrupacion5 = (
        filtro5.groupby("nombre")["id"]
        .count()
        .reset_index(name="conteo")
        .sort_values("conteo", ascending=False)
    )

    agrupacion_resumen = {
        "agrupacion1": agrupacion1,
        "agrupacion2": agrupacion2,
        "agrupacion3": agrupacion3,
        "agrupacion4": agrupacion4,
        "agrupacion5": agrupacion5
    }

    return agrupacion_resumen