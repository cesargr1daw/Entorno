#Ejercicio 1: Crea un programa en Python que escriba en pantalla el producto de dos números prefijados.
Numero1= 3
Numero2= 2
producto= Numero1*Numero2
print ("El producto de"+ (str (Numero1))+ "por"+ (str(Numero2))+ "seria"+(str(producto)))
#Ejercicio 2: Crea un programa que muestre el resto de dividir dos números prefijados.
Numero3= 8
Numero4= 4
Resto= Numero3/Numero4
print ("El resto de dividir"+(str(Numero3))+"entre"+(str(Numero4))+"seria"+(str(Resto)))
#Ejercicio 3: Crea un programa que calcule y muestre la media aritmética de dos números enteros introducidos por el usuario. Hay que tener en cuenta que la media aritmética puede contener decimales.
Var1= int (input ("Primer numero"))
Var2= int (input ("Segundo numero ")) 
Var3=2
MediaAritmetica= (Var1+Var2)/Var3
print ("La Media aritmetica de"+(str(Var1)) +"y"+(str(Var2))+"seria="+(str(MediaAritmetica)))
#Ejercicio 4: Crea un programa que pida al usuario una longitud en millas (por ejemplo, 3) y calcule su equivalencia en metros (1 milla = 1609 m).
LongitudEnMillas= float (input("Numero de Millas "))
Variable1=1609
Producto= LongitudEnMillas*float(Variable1)
print ((str (LongitudEnMillas)+"Millas")+ "serian"+(str(Producto))+"metros")
#Ejercicio 5: Crea un programa que pida al usuario una temperatura en grados centígrados y calcule (y muestre) a cuántos grados Fahrenheit equivalen (F =9*C/5 + 32).
Temperatura= float (input ("Grados Centigrados"))
Numero=32
Fahr=(9*Temperatura/5)+Numero
print ((str(Temperatura)+"Grados centigrados equivalen a"+(str(Fahr))+"Grados Fahrenheit"))
#Ejercicio 6: Realiza un programa que pida al usuario cuatro notas decimales y muestre la parte entera de su media aritmética.
Nota1= float(input("Nota 1"))
Nota2= float(input("Nota 2"))
Nota3= float(input("Nota 3"))
Nota4= float(input("Nota 4"))
Var4=4
Aritmetica=(Nota1+Nota2+Nota3+Nota4)/Var4
print (float (Aritmetica))
#Ejercicio 7: Realiza un programa en Python que pida al usuario la base y altura de un triángulo y muestre su área.
Base= float (input ("Base del triangulo"))
Altura= float (input ("Altura del triangululo"))
Area= Base*Altura/2
print ("El area del triangulo seria, ", Area)

#Ejercicio 8 Realizar un programa que lea una cantidad de horas, minutos y segundos, y los transforme en una expresión de tiempo convencional en la que los minutos y segundos estén dentro del rango [0,59]. Por ejemplo, dadas
#10 horas, 119 minutos y 280 segundos, debería dar como resultado 12 horas,3 minutos y 40 segundos
horas= int (input ("Cantidad de horas"))
minutos= int (input ("Cantidad de minutos"))
segundos= int (input ("cantidad de segundos"))
NuevosSegundos= segundos%60
NuevosMinutos=(NuevosSegundos+minutos)//60
NuevasHoras=(NuevosMinutos+horas)
print (NuevasHoras,("Horas,"),NuevosMinutos,("Minutos,"),NuevosSegundos,("Segundos."))