import pandas as pd
from utils.simulador_usuarios import simular_usuarioss

simulaciones = simular_usuarioss(10)
simulaciones_ordenadas = pd.DataFrame(simulaciones)

#convirtiendo  nuestra simulacion en dos formatos diferentes
#JSON
simulaciones_ordenadas.to_json("Data/SimulacionUsuarios.json", orient="records", indent=4)
#CSV
simulaciones_ordenadas.to_csv("Data/SimulacionUsuarios.csv")