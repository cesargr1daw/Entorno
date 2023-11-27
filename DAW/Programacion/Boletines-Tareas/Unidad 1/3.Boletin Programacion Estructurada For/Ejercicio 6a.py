#Ejercicio 6 Escribir una aplicación que pida un número n, y escriba los números desde 1 hasta n.
variable=0
Numero=int(input("Introduce un número"))
for variable in range (1,Numero+1,1):
    print (variable)