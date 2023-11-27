#Haz un programa que permita calcular la suma de dos números. Pedirá dos números al usuario y mostrará su suma, volviendo a repetir hasta que ambos 
#números introducidos sean 0.
Numero1=int(input ("Introduce un número:"))
Numero2=int (input ("Introduce otro número:"))
suma=0
while not (Numero1==0 and Numero2==0):
    Numero1=int(input ("Introduce un número:"))
    Numero2=int (input ("Introduce otro número:"))
    suma=Numero1+Numero2
    print (suma)