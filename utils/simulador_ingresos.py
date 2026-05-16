import random
from datetime import datetime, timedelta

def simular_ingresos(numeroIngresos):
    
    listaCategorias = ["intereses", "comisiones", "ventas", "creditos"]
    ListaDescripciones = ["pago de nomina", "rendimientos bancarios", "venta de servicios", "pago de cliente", "bono mensual"]
    
    Ingresos = []
    fecha_inicial = datetime(2010, 1, 1)

    for _ in range(numeroIngresos):
        
        fechaSimulada = fecha_inicial + timedelta(days=random.randint(0, 120))
        createdAtSimulada = fechaSimulada + timedelta(hours=random.randint(1, 8))

        ingreso = {
            "id": random.randint(1, 500), 
            "fecha": fechaSimulada.strftime("%Y-%m-%d %H:%M:%S"), 
            "valor": random.randint(100000, 50000000),
            "descripcion": random.choice(ListaDescripciones), 
            "categoria": random.choice(listaCategorias),
            "cliente_id": random.randint(1, 20), 
            "created_at": createdAtSimulada.strftime("%Y-%m-%d %H:%M:%S") 
        }

        ## --- INYECTAR ERRORES CONTROLADOS ---
        probabilidadError = random.random()

        if probabilidadError < 0.1:
            # Error tipo 1: IDs corruptos y valores nulos
            ingreso["id"] = random.choice([None, -1, 0])
            ingreso["valor"] = None
            
        elif probabilidadError < 0.3:
            # Error tipo 2: Espacios en blanco innecesarios (Limpia con .strip() en tu limpieza)
            ingreso["descripcion"] = " " + ingreso["descripcion"] + " "
            
        elif probabilidadError < 0.6:
            # Error tipo 3: Inconsistencia de mayúsculas (Limpia con .lower() o .upper() en tu limpieza)
            ingreso["categoria"] = ingreso["categoria"].upper()
            
        elif probabilidadError < 0.9:
            # Error tipo 4: Fechas nulas 
            # IMPORTANTE: Ponemos ambas en None para que el flujo de limpieza las maneje consistentemente
            ingreso["fecha"] = None 
            ingreso["created_at"] = None     

        Ingresos.append(ingreso)
        
    return Ingresos