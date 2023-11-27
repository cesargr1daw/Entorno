#Construye un programa que calcule el resultado de un número elevado a otro
#número. Ambos números deben recibirse por teclado. Deberás calcular el
#resultado realizando multiplicaciones y no el operador ** (potencia)
Numero=int(input("Introduce un número"))
Elevado=int(input("Elevado a "))
producto=1
contador=0
while Elevado!=contador:
    producto=producto*Numero
    contador=contador+1
print (producto)