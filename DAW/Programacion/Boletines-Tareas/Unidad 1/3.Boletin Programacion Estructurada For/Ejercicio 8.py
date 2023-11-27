#Ejercicio 8 Diseñar un programa que muestre el producto de los 10 primeros números impares
variable=0
producto=1
for variable in range (1,21,2):
    producto*=variable
print (producto)
#Otra
variable=0
producto=1
for variable in range (1,21,2):
    producto=producto*variable
print (producto)
#Otra forma
variable=0
producto=1
for variable in range (1,21):
    if variable%2!=0:
        producto*=variable
        print (producto)