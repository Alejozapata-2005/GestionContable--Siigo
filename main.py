import pandas as pd

from notebook.limpieza_usuarios import limpiar_datos
from utils.simulador_usuarios import simular_usuarioss


simulaciones = simular_usuarioss(1000)

#llamando a panda para crear data frame de los datos de entrada
simulaciones_ordenadas = pd.DataFrame(simulaciones)

#llamando a la rutina de limpieza
simulaciones_limpias = limpiar_datos(simulaciones_ordenadas)

print(simulaciones_limpias)



##Llamado a ingresos

# Se cambian las importaciones para apuntar a los nuevos archivos de transacciones/registros

import pandas as pd  # ¡Faltaba esta línea!

from notebook.Limpieza_ingresos import limpiar_datos
from utils.simulador_ingresos import simular_ingresos

simulaciones = simular_ingresos(1000)

# llamando a panda para crear data frame de los datos de entrada
simulaciones_ordenadas = pd.DataFrame(simulaciones)

# llamando a la rutina de limpieza
simulaciones_limpias = limpiar_datos(simulaciones_ordenadas)

print(simulaciones_limpias)