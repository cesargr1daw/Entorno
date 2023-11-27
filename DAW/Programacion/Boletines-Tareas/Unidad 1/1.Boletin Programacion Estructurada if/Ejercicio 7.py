#Ejercicio 7 Realizar un programa que solicite dos números por teclado e imprima en pantalla si son iguales
Numero1=int(input("Primer número "))
Numero2=int(input("Segundo número "))
if Numero1==Numero2:
    print ("Ambos son iguales")
else:
    if Numero1>Numero2:
        print (Numero1, "es mayor que", Numero2)
    if Numero1<Numero2:
        print (Numero1, "es menor que", Numero2)