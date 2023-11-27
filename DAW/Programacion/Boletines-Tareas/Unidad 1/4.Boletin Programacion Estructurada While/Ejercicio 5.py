#Escribe un programa que pida al usuario un número y devuelva la tabla de múltiplicar de ese número del 1 al 10
Numero=int (input("Introduce un numero:"))
producto=1
while Numero>0:
    producto=producto*Numero
    print (producto)
    Numero=int (input("Introduce un numero:"))