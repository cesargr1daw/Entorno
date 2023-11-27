#Ejercicio 13 Realizar un programa que lea un carácter y dos números enteros por teclado.Si el carácter leído es un operador aritmético, calcular la operación correspondiente, si es cualquier otro debe mostrar un error.
var1=int(input("Primer número:"))
Caracter=str(input("Introduce un caracter:")).upper ()
var2=int (input("Segundo número:"))
if Caracter== "+"or"-"or"*"or"/":
    if Caracter== "+":
        print ("igual a:",var1+var2)
    elif Caracter=="-":
        print("igual a:",var1-var2)
    elif Caracter=="*":
        print ("igual a:",var1*var2)
    elif Caracter=="/":
        print ("igual a:",var1/var2)
    else:
     print ("Error")