#Construye un programa que te pida un nombre. Sólo si el nombre introducido se corresponde con el del usuario a logar, nos pide la clave de dicho usuario.
#Si ambas cosas son correctas, imprime “Usuario logado correctamente”. Sino se corresponde seguirá pidiéndonos el nombre de la misma forma que si 
#la clave no se corresponde

Usuario=str(input("Introduce usuario:"))
while Usuario!="Oscar":
    print ("Error Usuario")
    Usuario=str(input("Introduce Usuario:"))
contraseña=int (input("Contraseña:"))
while contraseña!=1234:
    print("Error contraseña")
    contraseña= int (input("Contraseña:"))
else:
    print ("Logado correctamente")