Usuario=str(input("Introduce el Usuario:"))
while Usuario!="oscar":
    print("Usuario incorrecto")
    Usuario=str(input("Introduce el Usuario:"))
Contraseña=int(input("Introduce la contraseña:"))
while Contraseña!=1234:
    print("Contraseña incorrecta")
    Contraseña=int(input("Introduce la contraseña:"))
else:
    print("Usuario logado correctamente")