temperatura = float (input("La temperatura de la sala es: "))
if temperatura > 26 : #devuelve True
    print("Encendiendo aire acondicionado")
    print ("Sistema monitorizado automaticamente") 
    temperatura = float (input("La temperatura de la sala es: "))
    if temperatura < 23 :
     print ("Apago el aire")
print("Registrada:"+ str(temperatura))