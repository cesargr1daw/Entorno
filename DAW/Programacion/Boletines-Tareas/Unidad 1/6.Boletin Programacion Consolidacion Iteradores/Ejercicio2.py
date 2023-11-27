#Construye un programa que dado un número me pinte un cuadrado con tantos * por fila como ese número. Por ejemplo, para número = 4
numero=int(input("Número"))
cadena="*"
for numero in range (1,numero):
    for numero in range(1,numero):
        print (cadena)
    cadena=cadena+"*"