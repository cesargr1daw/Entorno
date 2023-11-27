#Construye un programa que pinte todas las tablas de multiplicar del 1 al 10.
numero1=1
numero2=1
producto=1
for numero1 in range(0,10):
    for numero2 in range (0,11):
        producto=numero1*numero2
        print (numero1, "x", numero2, "=",producto)