#Ejercicio 6 Modifica el programa anterior para que además nos muestre si el número es impar.
Numero=int (input ("Escribe un número "))
if Numero%3==0 and Numero%2==0 :
    print (Numero, " Es múltiplo de 3 y de 2.")
else:
    print (Numero, " No es múltiplo de 3 y de 2")
if (Numero%3==0 and Numero%2==0 ) and Numero%2==0 :
    print ("El número es par")
    if Numero%6==0:
        print ("El número es múltiplo de 6")
else:
    (Numero%3==0 and Numero%2==0 ) and Numero%2!=0
    print ("El número es impar")