#Diseña un programa que lee un número y calcula el número elevado a 2. 
#El programa deja de calcular cuadrados cuando el usuario introduce un número negativo.
Numero=int (input("Introduce un número:"))
while Numero>=0:
    print ("El cuadrado de",Numero, "es", +Numero*Numero)
    Numero=int (input("Introduce un número:"))
else:
    print("Número negativo")