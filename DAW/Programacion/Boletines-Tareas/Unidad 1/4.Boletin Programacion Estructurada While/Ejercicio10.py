#Ejercicio 10 While
import random
Maquina1=random.randint(0,100)
Maquina2=random.randint(0,100)
Usuario=int (input("Introduce un númmero"))
contador=1
suma=Maquina1+Maquina2
print(suma)#He incluido el print suma para tener la solución, si no la queremos eliminamos esta linea.

while Usuario!=suma:
    print("Incorrecto")
    Usuario=int(input("Introduce otro numero"))
    contador+=1
else:
    print ("Has acertado pero has necesitado",contador,"Intentos")