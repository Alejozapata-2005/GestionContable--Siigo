import pandas as pd

from notebook.limpieza_usuarios import limpiar_datos
from utils.simulador_usuarios import simular_usuarioss

#NUEVOusuario
##zona para importar llamados al api (consumos)
from notebook.consumo_usuario import consumir_api_tabla_usuarios
from notebook.consumo_Ingresos import consumir_api_tabla_Ingresos

#NUEVO
#cargando los datos del api
print("\n========== DATOS DE USUARIO ==========")
datos_API=consumir_api_tabla_usuarios()
print(datos_API)

#NUEVO Ingresos
#cargando los datos del api de ingresos
print("\n========== DATOS DE INGRESOS ==========")
datos_API_Ingresos=consumir_api_tabla_Ingresos()
print(datos_API_Ingresos)

simulaciones = simular_usuarioss(1000)

#llamando a panda para crear data frame de los datos de entrada
simulaciones_ordenadas = pd.DataFrame(simulaciones)

#llamando a la rutina de limpieza
simulaciones_limpias_usuarios = limpiar_datos(simulaciones_ordenadas)

print("\n========== USUARIOS LIMPIOS ==========")
print(simulaciones_limpias_usuarios)

from notebook.descripcion_usuario import describir_datos
##Llamado a ingresos

# Se cambian las importaciones para apuntar a los nuevos archivos de transacciones/registros

import pandas as pd  # ¡Faltaba esta línea!

from notebook.Limpieza_ingresos import limpiar_datos
from utils.simulador_ingresos import simular_ingresos

##Zona para importar descripciones 
from notebook.Descripcion_ingresos import describir_datos

simulaciones = simular_ingresos(1000)

# llamando a panda para crear data frame de los datos de entrada
simulaciones_ordenadas = pd.DataFrame(simulaciones)

# llamando a la rutina de limpieza
simulaciones_limpias_ingresos = limpiar_datos(simulaciones_ordenadas)

print("\n========== INGRESOS LIMPIOS ==========")
print(simulaciones_limpias_ingresos)

#describir_datos(simulaciones_limpias_usuarios)
