#Ejercicio 4 Dada las edades y las alturas de 4 alumnos, construye un programa que te diga los alumnos que son mayores de 18. Luego que te diga los que miden
#menos de la media.

Edad1=19
Edad2=12
Edad3=14
Edad4=20
Altura1=185
Altura2=170
Altura3=155
Altura4=165
mediaAltura=(Altura1+Altura2+Altura3+Altura4)/4
print (mediaAltura)
if Edad1>=18:
    print ("El alumno 1 es mayor de edad")
if Edad2>=18:
    print ("El alumno 2 es mayor de edad")
if Edad3>=18:
    print ("El alumno 3 es mayor de edad")
if Edad4>=18:
    print ("El alumno 4 es mayor de edad")

if Altura1<mediaAltura:
    print ("El alumno 1 mide menos que la media")
if Altura2<mediaAltura:
    print ("El alumno 2 mide menos que la media")
if Altura3<mediaAltura:
    print ("El alumno 3 mide menos que la media")
if Altura4<mediaAltura:
    print ("El alumno 4 mide menos que la media")