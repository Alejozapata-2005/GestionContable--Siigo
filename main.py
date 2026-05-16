import pandas as pd
from notebook.consumo_Ingresos import consumir_api_tabla_Ingresos
from notebook.Limpieza_ingresos import limpiar_datos 
from notebook.transformacion_ingresos import transformar_datos

datos_tabla_Ingresos = consumir_api_tabla_Ingresos()
data_frame_ingresos = pd.DataFrame(datos_tabla_Ingresos)
data_frame_limpio_ingresos = limpiar_datos(data_frame_ingresos)
agrupaciones = transformar_datos(data_frame_limpio_ingresos)
print(agrupaciones)