#10.Realizar un programa que solicite 4 números e imprima la media de los números. También debe imprimir aquellos números que son superiores a la media
Numero1= int (input("Numero 1:"))
Numero2= int (input("Numero 2:"))
Numero3= int (input("Numero 3:"))
Numero4= int (input("Numero 4:"))
Media=(Numero1+Numero2+Numero3+Numero4)/4
print ("La media es", Media)

if Numero1>Media :
    print (Numero1,"Superior a la media")
if Numero2>Media :
    print (Numero2,"Superior a la media")
if Numero3>Media :
    print (Numero3,"Superior a la media")
if Numero4>Media :
    print (Numero4,"Superior a la media")   