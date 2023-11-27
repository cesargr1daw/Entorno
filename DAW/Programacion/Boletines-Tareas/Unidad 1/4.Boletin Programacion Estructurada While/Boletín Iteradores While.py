#Ejercicio 3: Muestra los números del 10 al 1 en orden descendente utilizando un bucle while.
Numero=10
while Numero>0:
    print (Numero)
    Numero-=1
#Ejercicio 4 Construye un programa que pida al usuario que ingrese números hasta que ingrese un cero y luego muestra la suma de los números ingresados.
Numero=int (input("Introduce un número:"))
Suma=0
while Numero!=0:
    Numero=int (input("Introduce un número:"))
    Suma=Suma+Numero
    print(Suma)
else:
    print("He terminado")
#Otra opcion
Numero=int (input("Introduce un número:"))
Suma=0
while Numero!=0:
    Numero=int (input("Introduce un número:"))
    Suma=Suma+Numero
print(Suma)
#Ejercicio 5 Escribe un programa que pida al usuario un número y devuelva la tabla de múltiplicar de ese número del 1 al 10
Numero=int (input("Introduce un número:"))
Numero2=1
producto=1
while Numero2<11:
    print (Numero,"x",Numero2,"=",producto)
    Numero2+=1
    producto=Numero*Numero2
#Ejercicio 6 Haz un programa que permita calcular la suma de dos números. Pedirá dos números al usuario y mostrará su suma, volviendo a repetir hasta que ambos 
#números introducidos sean 0.
Numero1=int(input ("Introduce un número:"))
Numero2=int (input ("Introduce otro número:"))
suma=0
while not (Numero1==0 and Numero2==0):
    Numero1=int(input ("Introduce un número:"))
    Numero2=int (input ("Introduce otro número:"))
    suma=Numero1+Numero2
    print (suma)
#Ejercicio 7 Crea un programa que seleccione un número aleatorio y el usuario debe adivinarlo. El bucle while se ejecuta hasta que el usuario adivine
#correctamente.
import random
maquina=random.randint(0,10)
persona=int (input("Dime que numero ha pensado la maquina:"))
numerointento=1
while maquina!=persona:
    persona=int(input("Dime que numero ha pensado la maquina"))
    numerointento+=1
print("Has acertado, era el", maquina, "en el intento",numerointento)   
#Ejericico 8 Crea un programa que escriba los múltiplos del 3, desde el 3 hasta el 30, Pista utiliza un incremento por iteración de 3
numero=3
while numero<31:
    print (numero)
    numero=numero+3
#Ejercicio 9 Construye un programa que pida al usuario una contraseña, de forma repetitiva mientras que no introduzca "1234". Cuando finalmente escriba la contraseña correcta, se le dirá "Bienvenido" y terminará el programa.
Contraseña=int (input("Introduce la contraseña"))
while Contraseña!=1234:
    print ("Incorrecta")
    Contraseña=int (input("Introduce la contraseña"))
else:
    print("Bienvenido")
#Ejercicio 10 Crea un programa que genere dos números al azar entre el 0 y el 100, y pida al usuario que calcule e introduzca su suma. Si la respuesta no es correcta,
#deberá volver a pedirla tantas veces como sea necesario hasta que el usuarioacierte. Pista: usa la función random.randint(0, 100)
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