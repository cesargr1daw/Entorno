#5. Modifica el programa anterior para que nos diga: Si es par en ese caso mire si, además, es múltiplo de 6.Si es múltiplo de 6 → imprime múltiplo de 6
Numero= int(input("Introducir numero"))
if Numero % 2 == 0:
    print ("Es par")
    if Numero % 6 == 0 :
     print ("multiplo de 6")

#4. Lea un número por teclado y nos diga si o no múltiplo de 3 y de 2.
Numero= int(input("Introducir numero"))
if Numero %3==0 and Numero %2==0 :
   print ("Si")
else:
   print("No")