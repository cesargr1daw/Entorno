#Ejercicio 1 Lea por teclado un número correspondiente a un mes. Si el valor introducido es menor que 12 debe decir “valor correcto”.
Dia=int (input ("Dia del mes "))
if Dia<12:
    print ("Valor correcto")
#Ejercicio2 Modifica el programa anterior para incluir otra condición que nos diga,además, si el número es menor que 6
Dia=int (input ("Dia del mes "))
if Dia<12:
    print ("Valor correcto")
    if Dia<6: 
        print("El numero es menor que 6")
#Ejercicio 3 Lea un número entero por teclado y nos diga si es par, el cero se considera par. Pista Operador % = 0
Numero=int (input ("Escribe un numero "))
if Numero%2==0:
    print ("El numero es par.")
#4. Lea un número por teclado y nos diga si o no múltiplo de 3 y de 2.
Numero=int (input ("Escribe un numero "))
if Numero%3==0 and Numero%2==0 :
    print (Numero, " Es multiplo de 3 y de 2.")
else:
    print (Numero, " No es multiplo de 3 y de 2")
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
#Ejercicio 8 Realizar un programa que lea un número por teclado. El programa debe imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3 deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos el programa finaliza sin mostrar ningún mensaje.
Numero=int (input("Escribe un número"))
if Numero%2==0:
    print ("El número",Numero, "es múltiplo de 2.")
if Numero%3==0:
    print ("El número",Numero, "es múltiplo de 3.")
#Ejercicio 9 Realizar un programa que lea la edad de una persona menor a 100 años einforme de si es un niño (0-12 años), un adolescente (13-17), un joven (18-29) o un adulto.
Años=int (input ("Años"))
if Años<100:
    if Años>=0 and Años<=12:
        print ("Es un niño")
    else:
        if Años>=13 and Años<=17:
            print ("Es un adolescente")
        else:
            if Años>=18 and Años<=29:
                print ("Es un joven")
            else:
                Años>=30 and Años<=99
                print ("Es un Adulto")
#10.Realizar un programa que solicite 4 números e imprima la media de los números. También debe imprimir aquellos números que son superiores a la media
Numero1= int (input("Numero 1:"))
Numero2= int (input("Numero 2:"))
Numero3= int (input("Numero 3:"))
Numero4= int (input("Numero 4:"))
Media=(Numero1+Numero2+Numero3+Numero4)/4
print ("La media es", Media)

if Numero1>Media :
    print (Numero1,"Superior a la media")
if Numero2>Media :
    print (Numero2,"Superior a la media")
if Numero3>Media :
    print (Numero3,"Superior a la media")
if Numero4>Media :
    print (Numero4,"Superior a la media")
#Ejercicio 11  Realizar un programa que solicite un carácter por teclado e informe por pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará elmensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc
Caracter=input ("Introduce un caracter")
if Caracter == "a" or "A": 
    print ("vocal a")
else:
    if Caracter == "e" or "E":
        print ("vocal e")
    else:
        if Caracter == "o" or "O":
            print ("vocal o")
        else: 
            if Caracter == "i" or "I":
                print ("vocal i")
            else:
                if Caracter == "u" or "U":
                    print ("Vocal u")

#Ejercicio 11  Realizar un programa que solicite un carácter por teclado e informe por pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará elmensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc
Caracter= input ("Introduce un caracter")
if Caracter == "a" or "A": 
    print ("vocal a")
elif Caracter == "e" or "E":
    print ("vocal e")
elif Caracter == "o" or "O":
    print ("vocal o")
elif Caracter == "i" or "I":
    print ("vocal i")
elif Caracter == "u" or "U":
    print ("Vocal u")
#Ejercicio 12 Realizar un programa que lea el estado civil de una persona (S-Soltero, CCasado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por pantalla el porcentaje de retención que debe aplicarse de acuerdo con las siguientes reglas:
Estado=str(input("Estado Civil: ")).upper()
Edad=int (input ("Introducir la Edad"))
if Estado=="S"and Edad<35 or Estado=="D" and Edad<35:
    print ("12%")
elif Estado and Edad>50:
    print ("8.5%")
elif Estado=="V"and Edad<35 or "C" and Edad<35:
    print ("11.3%")
else:
    print ("10.5%")
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
#14.Escribe un programa que tome la calificación de un examen como entrada y muestre la calificación equivalente en letras (A, B, C, D o F) según la siguiente escala: 90-100 A, 80-89 B, 70-79 C, 60-69 D, por debajo de 60 F.
Calificacion=int(input("Introduce la calificación:"))
if Calificacion==100 and Calificacion>=90:
    print ("A")
elif Calificacion<=89 and Calificacion>=80:
    print ("B")
elif Calificacion<=79 and Calificacion>=70:
    print ("C")
elif Calificacion<=69 and Calificacion>=60:
    print ("D")
elif Calificacion<=59 and Calificacion>=0:
    print ("F")