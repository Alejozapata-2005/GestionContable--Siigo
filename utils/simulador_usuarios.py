import random
import string

def simular_usuarios(numeroUsuarios):
    listaUsuarios=["Sahara", "Alejo","Samiris","Carlos"," Ana","luis"]

    correos=["sahara@gmail.com","alejo@yahoo.com","samiris@outlook.com","carlos@empresa.com"]

    roles=["admin","usuario","gerente"," contador"]

    Usuarios=[]
    for _ in range (numeroUsuarios):
        nombre=random.choice(nombre)
        Usuarios={

            "id":random.randint(0,5000),
            "nombre":random.choice(listaUsuarios),
            "rol":random.choice(roles),
            "correo":random.choice(correos)
                      

        }

        Usuarios.append(Usuarios)
        return Usuarios