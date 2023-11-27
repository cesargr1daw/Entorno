#Escribe un programa que trabaje como una caja registradora. El usuario introducirá precios de productos y el sistema irá sumando cada precio. El
#sistema sabrá que debe imprimir el resultado de la suma cuando el usuario introduzca un valor negativo.

precio=float(input("Precio del producto:"))
suma=0
while precio>0: 
   suma=suma+precio
   precio=float(input("Precio del producto:"))  
print ("El precio total es",suma, "Euros")