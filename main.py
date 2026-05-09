import pandas as pd

from notebook.limpieza_usuarios import limpiar_datos
from utils.simulador_usuarios import simular_usuarioss

#NUEVOusuario
##zona para importar llamados al api (consumos)
from notebook.consumo_usuario import consumir_api_tabla_usuarios

#NUEVO
#cargando los datos del api
datos_API=consumir_api_tabla_usuarios()
print(datos_API)

simulaciones = simular_usuarioss(1000)

#llamando a panda para crear data frame de los datos de entrada
simulaciones_ordenadas = pd.DataFrame(simulaciones)

#llamando a la rutina de limpieza
simulaciones_limpias_usuarios = limpiar_datos(simulaciones_ordenadas)

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

#describir_datos(simulaciones_limpias_ingresos)

#describir_datos(simulaciones_limpias_usuarios)
