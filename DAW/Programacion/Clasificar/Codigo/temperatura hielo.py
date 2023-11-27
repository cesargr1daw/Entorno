temperatura = 23
if temperatura > 26 :#cond1 == true
    print("Encendiendo aire acondic")
elif temperatura < 16 : #cond2 == true
    print("Encendiendo calefacción")
    if temperatura < 0:
        print ("Alerta hielo")
else:
    print ("Temperatura registrada:"+ str(temperatura))