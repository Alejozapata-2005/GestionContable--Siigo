import pandas as pd
from notebook.consumo_Ingresos import consumir_api_tabla_Ingresos
from notebook.Limpieza_ingresos import limpiar_datos as limpiar_datos_ingresos  # Alias aplicado
from notebook.transformacion_ingresos import transformar_datos_ingresos
from notebook.consumo_usuario import consumir_api_tabla_usuarios
from notebook.limpieza_usuarios import limpiar_datos as limpiar_datos_usuarios  # Alias aplicado
from notebook.transformacion_usuario import transformar_datos as transformar_datos_usuarios
from notebook.Graficacion import graficar_lineas, graficar_barras, graficar_torta, graficar_mapa_calor

## Tabla ingresos
datos_tabla_Ingresos = consumir_api_tabla_Ingresos()
data_frame_ingresos = pd.DataFrame(datos_tabla_Ingresos)
data_frame_limpio_ingresos = limpiar_datos_ingresos(data_frame_ingresos)      
agrupaciones_ingresos = transformar_datos_ingresos(data_frame_limpio_ingresos)

## Tabla Usuarios
datos_tabla_usuarios = consumir_api_tabla_usuarios()
data_frame_usuarios = pd.DataFrame(datos_tabla_usuarios)
data_frama_limpio_usuarios = limpiar_datos_usuarios(data_frame_usuarios)      
agrupaciones_usuarios = transformar_datos_usuarios(data_frama_limpio_usuarios)


## grafica 1
graficar_barras(
    agrupaciones_ingresos["conteo_altos_ingresos"],  
    columna_categorias="categoria",                   
    columna_valores="conteo_transacciones_altas",                
    titulo="Conteo de Transacciones Altas (>=500k) por Categoría",
    color_barras="#4CAF50",  
    nombre_archivo="barras_conteo_altos_ingresos.png"
)


graficar_lineas(
    agrupaciones_ingresos["ventas_diarias"],  
    columna_eje_x="fecha",             
    columna_eje_y="total_ventas_diarias", 
    titulo="Evolución de Ventas Diarias",
    color_linea="#E91E63",  
    nombre_archivo="lineas_ventas_diarias.png"
)

graficar_barras(
    agrupaciones_ingresos["auditoria_cliente"],  
    columna_categorias="cliente_id",                   
    columna_valores="monto_maximo",                
    titulo="Monto Máximo Registrado por Cliente",
    color_barras="#9C27B0",  
    nombre_archivo="barras_auditoria_maximos_cliente.png"
)


