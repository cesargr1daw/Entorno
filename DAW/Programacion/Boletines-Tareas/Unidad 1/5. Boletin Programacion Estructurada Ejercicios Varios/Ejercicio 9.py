#Modifica tu programa para que también lleve la cuenta del impuesto total (7%). Al terminar el programa mostrará lo que el cliente debe pagar por su
#compra (suma) y qué cantidad se corresponde con el IVA

precio=float(input("Precio del producto: "))
suma=0
impuesto=0.07
   
while precio>0:
    
    suma=suma+precio
    iva=suma*impuesto
    Total=suma+iva  
    precio=float(input("Precio del producto: "))   
print ("El precio de los productos es", suma)
print ("El IVA es", iva)
print ("Total mas IVA",Total)

#Otra forma diferente pero creo que no correcta al estar todo junto.
precio=float(input("Precio del producto:"))
suma=0
while precio>0:
    suma=suma+precio+(precio*0.07)
    precio=float(input("Precio del producto:")) 
print ("El precio total es",suma, "Euros")