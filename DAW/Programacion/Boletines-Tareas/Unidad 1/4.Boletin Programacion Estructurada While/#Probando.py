#Muestra los números del 10 al 1 en orden descendente utilizando un bucle while.
Numero=10
while Numero>0:
    print (Numero)
    Numero-=1
#Construye un programa que pida al usuario que ingrese números hasta que ingrese un cero y luego muestra la suma de los números ingresados.
Numero=int (input("Introduce un número:"))
Suma=0
while Numero!=0:
    Numero=int (input("Introduce un número:"))
    Suma=Suma+Numero
    print(Suma)
else:
    print("He terminado")
#Escribe un programa que pida al usuario un número y devuelva la tabla de múltiplicar de ese número del 1 al 10
Numero=int (input("Introduce un número:"))
Numero2=1
producto=1
while Numero2<11:
    print (Numero,"x",Numero2,"=",producto)
    Numero2+=1
    producto=Numero*Numero2
