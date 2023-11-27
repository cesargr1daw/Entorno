#Ejercicio 10
num=13
contador=0
for divisor in range (2,13):
    if num%divisor==0:
        print ("No primo",divisor)
    contador=1+contador
if contador ==0:
    print ("primo")