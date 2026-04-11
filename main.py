import pandas as pd
from utils.simulador_usuarios import simular_usuarioss
from utils.simulador_ingresos import simular_ingresos

simulaciones = simular_usuarioss(10)
simulaciones_ordenadas = pd.DataFrame(simulaciones)

#convirtiendo  nuestra simulacion en dos formatos diferentes
#JSON
simulaciones_ordenadas.to_json("Data/SimulacionUsuarios.json", orient="records", indent=4)
#CSV
simulaciones_ordenadas.to_csv("Data/SimulacionUsuarios.csv")


SimulacionCreacion = simular_ingresos(10)
simulaciones_Ingresos = pd.DataFrame(SimulacionCreacion)

#convirtiendo  nuestra simulacion en dos formatos diferentes
#JSON
simulaciones_Ingresos.to_json("Data/SimulacionIngresos.json", orient="records", indent=4)
#CSV
simulaciones_Ingresos.to_csv("Data/SimulacionIngresos.csv")
