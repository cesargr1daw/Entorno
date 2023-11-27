# Ejercicio 5 Modifica el programa anterior para que nos diga:
Numero=int (input ("Escribe un número "))
if Numero%3==0 and Numero%2==0 :
    print (Numero, " Es múltiplo de 3 y de 2.")
else:
    print (Numero, " No es múltiplo de 3 y de 2")
if (Numero%3==0 and Numero%2==0 ) and Numero%2==0 :
    print ("El número es par")
    if Numero%6==0:
        print ("El número es múltiplo de 6")