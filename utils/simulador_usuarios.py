import random
import string

def simular_usuarioss(numerousuarioss):
    listausuarioss=["Sahara", "Alejo","Samiris","Carlos"," Ana","luis"]

    correos=["sahara@gmail.com","alejo@yahoo.com","samiris@outlook.com","carlos@empresa.com"]

    roles=["admin","contador","gerente"," contador"]

    usuarios=[]
    for _ in range (numerousuarioss):
        nombre=random.choice(listausuarioss)
        usuario={

            "id":random.randint(0,5000),
            "nombre":random.choice(listausuarioss),
            "rol":random.choice(roles),
            "correo":random.choice(correos)
                      

        }
        #Inyectando errores controlados
        probabilidadError=random.random()
        if probabilidadError<0.1:
            usuario["id"]=random.choice([None,-1,0])
            #usuario["nombre"]=None

        elif probabilidadError<0.3:
            usuario["rol"]= " "+usuario["rol"]+ " "
        elif probabilidadError<0.6:
            usuario["correo"]= usuario["correo"].upper()
      
   


        usuarios.append(usuario)
    return usuarios
