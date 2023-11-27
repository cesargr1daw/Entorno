#Vamos a calcular si existe algun numero que divida a 58 y que no sea ni 58 ni 1 (Primo)
cuentanumerodevecesqueentroenif=0
for divisor in range (2,57,1):
    if 58%divisor==0:
        print ("El 58 es divisible por", divisor)
        cuentanumerodevecesqueentroenif=cuentanumerodevecesqueentroenif+1
        #cuentanumerodevecesqueentroenif guarda cuantos numeros son divisores de 58 y no son el 58 ni el 1.
        print (cuentanumerodevecesqueentroenif)
#Ver si es primo el 58 y contador.
num=58
contador=0
for divisor in range (2,57):
    if num%divisor==0:
        print ("No primo",divisor)
    contador=1+contador
if contador ==0:
    print ("primo")