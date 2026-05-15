import requests
def consumir_api_tabla_Ingresos():
    

    #1. escribir la Url del servicio que quiero consumir
    url="http://localhost:8081/api/ingresos"

    #2. utilizar request de python para ir al API
    respuesta=requests.get(url)

    #3. Verifico la respuesta
    respuesta.raise_for_status()

    #4. verifico el formato de los datos recibidos
    datos=respuesta.json()

    return datos 
