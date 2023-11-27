#Ejercicio 3 Muestra los números del 10 al 1 en orden descendente utilizando la estructura for.
variable=1
for variable in range (10,0,-1):
    print (variable)
#Ejercicio 4 Escribe un programa que pida al usuario un número y devuelva la tabla de múltiplicar de ese número del 1 al 10
variable=0
Numero=int (input("Introduce un número"))
for variable in range (1,11,1):
    print (Numero*variable)
#Ejercicio 5 Crea un programa que eescriba los múltiplos del 3, desde el 3 hasta el 30, Pista utiliza un incremento por iteración de 3.
for numero in range (3,31,3):
    print (numero)
#Otra forma de hacerlo
for numero in range (1,31):
    print (numero*3)
#Ejercicio 6 Escribir una aplicación que pida un número n, y escriba los números desde 1 hasta n.
variable=0
Numero=int(input("Introduce un número"))
for variable in range (1,Numero+1,1):
    print (variable)
#Ejercicio 7 Escribir todos los múltiplos de 7 menores que 100.
variable=0
for variable in range (1,100):
    if variable%7==0:
     print (variable)
#Otra forma de hacerlo
variable=0
for variable in range (7,100,7):
   print (variable)
#Ejercicio 8 Diseñar un programa que muestre el producto de los 10 primeros números impares
variable=0
for variable in range (1,21):
    if variable%2!=0:
        print (variable)
#Ejercicio 9
factorial=int (input("Número:"))
variable=0
for variable in range (1,factorial,1):
    factorial=factorial*variable
    print (factorial)
#Ejercicio 10
