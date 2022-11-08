#ejercicio_18.py


from cola import Cola
import random


cola_turnos = Cola()
cola1 = Cola()
cola2 = Cola()
aux = Cola()


class turno():
    letras, numero= None, None

   

letras = ["A", "B", "C", "D", "E", "F"]
letra = letras[random.randint(0, 5)]
numero = (str(random.randint(0, 999))) 

#A
isertar= True

for i in range (20):
        dato=turno()
        dato.letras = letras[random.randint(0, 5)]
        dato.numero = numero

        cola_turnos.arribo(dato)
print(cola_turnos)


def desapilar_cola():

        cola1 = ["A", "C", "F"]
        cola2 = []
        while (not cola_turnos.cola_vacia()):
            aux=cola_turnos.atencion()
            if aux.numero in cola1:
                cola1.arribo(aux)
            else:
                cola2.arribo(aux)


#B
print (cola1)
print("---------------------------------------------------------------")

print(cola2)


#C

if (cola1.tamanio()>cola2.tamanio()):
  print("la cola con mas turnos es:",cola1)
else:
    print("la cola con mas turnos es:",cola2)


#D


if( (cola1<cola2) and (turno>506)):
  print(cola1)
else:
    if((cola2<cola1) and turno>506):
       print(cola2)



