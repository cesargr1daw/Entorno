#Ejercicio 7 Escribir todos los múltiplos de 7 menores que 100.
variable=0
for variable in range (1,100):
    if variable%7==0:
     print (variable)
#Otra forma de hacerlo
variable=0
for variable in range (7,100,7):
   print (variable)