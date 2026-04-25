import pandas as pd

from notebook.limpieza_usuarios import limpiar_datos
from utils.simulador_usuarios import simular_usuarioss


simulaciones = simular_usuarioss(1000)

#llamando a panda para crear data frame de los datos de entrada
simulaciones_ordenadas = pd.DataFrame(simulaciones)

#llamando a la rutina de limpieza
simulaciones_limpias = limpiar_datos(simulaciones_ordenadas)

print(simulaciones_limpias)
