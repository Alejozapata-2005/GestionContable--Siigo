import random
from datetime import datetime, timedelta

def simular_ingresos(numeroIngresos):
    
    
    listaCategorias = ["intereses", "comisiones", "ventas", "creditos"]
    
    # Descripciones ajustadas para que parezcan ingresos
    ListaDescripciones = ["pago de nomina", "rendimientos bancarios", "venta de servicios", "pago de cliente", "bono mensual"]
    
    Ingresos = []
    fecha_inicial = datetime(2010, 1, 1)

    for _ in range(numeroIngresos):
        
        fechaSimulada = fecha_inicial + timedelta(days=random.randint(0, 120))
        ingreso = {
            "id": random.randint(0, 20),
            "fecha": fechaSimulada.strftime("%d-%m-%y"),
            "valor": random.randint(100000, 50000000),
            "descripcion": random.choice(ListaDescripciones), # en minúscula para que Pandas no falle
            "categoria": random.choice(listaCategorias)       # en minúscula para que Pandas no falle
        }

        ## inyectar errores controlados 
        probabilidadError = random.random()

        if probabilidadError < 0.1:
            ingreso["id"] = random.choice([None, -1, 0])
            ingreso["valor"] = None
        elif probabilidadError < 0.3:
            ingreso["descripcion"] = " " + ingreso["descripcion"] + " "
        elif probabilidadError < 0.6:
            ingreso["categoria"] = ingreso["categoria"].upper()
        elif probabilidadError < 0.9:
            ingreso["fecha"] = None      

        Ingresos.append(ingreso)
        
    return Ingresos