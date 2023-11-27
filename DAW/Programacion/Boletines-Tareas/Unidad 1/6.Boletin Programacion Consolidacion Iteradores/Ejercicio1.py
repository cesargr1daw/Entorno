#Construye un programa que dado un número me devuelva un triángulo de *. Imagina que le damos el 5, la primera fila tendrá un *, dos la segunda, así
#hasta que la quinta tenga 5.
numero=int (input("Número:"))
cadena="*"
for numero in range (1,numero):
    print (cadena)
    cadena=cadena+"*"