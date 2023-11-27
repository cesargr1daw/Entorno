#Casa Rural
Listado=input("Listado de Habitaciones").upper()
match Listado:
    case Listado:
        print ("1.Azul")
        print ("2.Roja")
        print ("3.Verde")
        print ("4.Rosa")
        print ("5.Gris")
Habitacion=int (input ("Numero de Habitación:"))
if Habitacion==1:
    print ("Planta primera, Nº de camas 2")
elif Habitacion==2:
    print ("Primera planta, Nº de camas 1")
elif Habitacion==3:
    print ("Segunda planta, Nº de camas 3")
elif Habitacion==4:
    print ("Segunda planta, Nº de camas 2")
elif Habitacion==5:
    print ("Tercera planta, Nº de camas 1")
#Casa Rural
Listado="Listado"
match Listado:
    case Listado:
        print ("Listado de Habitaciones")
        print ("1.Azul")
        print ("2.Roja")
        print ("3.Verde")
        print ("4.Rosa")
        print ("5.Gris")
Habitacion=int (input ("Numero de Habitación:"))
match Habitacion:
    case 1:
        print ("Planta primera, Nº de camas 2")
    case 2:
        print ("Primera planta, Nº de camas 1")
    case 3:
        print ("Segunda planta, Nº de camas 3")
    case 4:
        print ("Segunda planta, Nº de camas 2")
    case 5:
        print ("Tercera planta, Nº de camas 1")