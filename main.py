import pandas as pd
from notebook.consumo_Ingresos import consumir_api_tabla_Ingresos
from notebook.Limpieza_ingresos import limpiar_datos 
from notebook.transformacion_ingresos import transformar_datos
from notebook.consumo_usuario import consumir_api_tabla_usuarios
from notebook.limpieza_usuarios import limpiar_datos
from notebook.transformacion_usuario import transformar_datos


datos_tabla_Ingresos = consumir_api_tabla_Ingresos()
data_frame_ingresos = pd.DataFrame(datos_tabla_Ingresos)
data_frame_limpio_ingresos = limpiar_datos(data_frame_ingresos)
agrupaciones_ingresos = transformar_datos(data_frame_limpio_ingresos)
datos_tabla_usuarios=consumir_api_tabla_usuarios()
data_frame_usuarios= pd.DataFrame(datos_tabla_usuarios)
data_frama_limpio_usuarios=limpiar_datos(data_frame_usuarios)
agrupaciones_usuarios=transformar_datos(data_frama_limpio_usuarios)




#Graficas#
graficar_lineas(
    agrupaciones_usuarios["agrupacion1"],
    columna_eje_x="dominio",
    columna_eje_y="conteo",
    titulo="Usuarios por dominio de correo",
    color_linea="#2196F3",
    nombre_archivo="lineas_usuarios_por_dominio.png"
)

graficar_barras(
    agrupaciones_usuarios["agrupacion2"],
    columna_categorias="nombre",
    columna_valores="conteo",
    titulo="Cantidad de usuarios por nombre",
    color_barras="#4CAF50",
    nombre_archivo="barras_usuarios_por_nombre.png"
)

graficar_torta(
    agrupaciones_usuarios["agrupacion3"],
    columna_etiquetas="tipo_correo",
    columna_valores="conteo",
    titulo="Proporción de usuarios por tipo de correo",
    nombre_archivo="torta_tipos_correo.png"
)

graficar_mapa_calor(
    agrupaciones_usuarios["agrupacion4"],
    columna_filas="dominio",
    columna_columnas="nombre",
    columna_valores="conteo",
    titulo="Cantidad de usuarios por dominio y nombre",
    paleta_color="YlOrRd",
    nombre_archivo="mapa_calor_usuarios_dominio_nombre.png"
)
