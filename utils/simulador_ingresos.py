import random
from datetime import datetime,timedelta


def simular_ingresos(numeroIngresos):
  
  listaCategorias=["intereses", "comisiones", "ventas", "creditos", "comisiones"]
  ListaDescripciones=["pago de nomina", "suscripcion spotify", "compra en macdonals", "compra de gasolina", "compra en exito"]
  Ingresos=[]
  fecha_inicial=datetime(2010,1,1)

  for _ in range (numeroIngresos):
    
    fechaSimulada=fecha_inicial+timedelta(days=random.randint(0,120))
    ingreso={
      "id":random.randint(0,20),
      "fecha":fechaSimulada.strftime("%d-%m-%y"),
      "valor":random.randint(100000,50000000),
      "Descripcion": random.choice(ListaDescripciones),
      "Categoria": random.choice(listaCategorias)

    }

    ##inyectar errores controlados 
    probabilidadError= random.random()

    if probabilidadError <0.1:
      ingreso["id"]=random.choice([None,-1,0])
      ingreso["valor"]=None
    elif probabilidadError <0.3:
      ingreso["Descripcion"]=" " + ingreso["Descripcion"] + " "
    elif probabilidadError <0.6:
      ingreso["Categoria"]=ingreso["Categoria"].upper()
    elif probabilidadError <0.9:
      ingreso["fecha"]=None      
      

    Ingresos.append(ingreso)
    
  return Ingresos

