#Vamos a calcular si existe algun numero que divida a 59 y que no sea ni 59 ni 1 (Primo)
for divisor in range (2,58):
    if 59%divisor==0:
        print ("El 59 es divisible por", divisor)
    else:
        print ("No divisible por", divisor)
#Vamos a calcular si existe algun numero que divida a 58 y que no sea ni 58 ni 1 (Primo)
for divisor in range (2,57,1):
    if 58%divisor==0:
        print ("El 58 es divisible por", divisor)
#Ver si es primo el 59
for divisor in range (2,58):
    if 59%divisor==0:
        print ("No primo", divisor)