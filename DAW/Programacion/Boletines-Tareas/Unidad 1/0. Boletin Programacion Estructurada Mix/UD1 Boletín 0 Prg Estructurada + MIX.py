#Crea un programa que pida un número al usuario y diga si es positivo.
Numero1=int(input("Escribe un numero"))
if Numero1>0 :
    print ("El numero es positivo")
#Crea un programa que pida un número al usuario y diga si es positivo o negativo. (Programación estructurada Alternativa compuesta)
Numero1=int(input("Escribe un numero"))
if Numero1>0 :
    print ("El numero es positivo")
elif Numero1<0 :
    print ("El numero es negativo")
#Crea un programa que pida un número al usuario y diga si es positivo,negativo o cero. (Programación estructurada Alternativa compuesta)
Numero1=int(input("Escribe un numero"))
if Numero1>0 :
    print ("El numero es positivo")
elif Numero1<0 :
    print ("El numero es negativo")
else  :
    print ("El numero es 0")
#Haz un programa que pida al usuario dos números y diga cuántos de ellos son positivos. (Programación estructurada Alternativa)
Numero1=int(input("Escribe un numero 1"))
Numero2=int(input("Escribe un numero 2"))
if Numero1>0 and Numero2 >0:
    print ("2")
elif Numero1<0 and Numero2>0:
    print ("1")
elif Numero1>0 and Numero2<0:
    print ("1")
else:
    print ("0")
#Haz un programa que pida al usuario dos números y diga cuántos de ellos son positivos. (Programación estructurada Alternativa) (Mas optimizado.)
Numero1=int(input("Escribe un numero 1"))
Numero2=int(input("Escribe un numero 2"))
if Numero1>0 and Numero2 >0:
    print ("2")
elif Numero1<0 and Numero2>0 or Numero1>0 and Numero2<0:
    print ("1")
else:
    print ("0")