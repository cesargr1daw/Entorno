import random 
maquina= random.randint (0, 2)
persona= input ("Piedra, papel o tijera").upper() #El upper podemos ponerlo en la variable
if maquina ==0:
    print ("Apuesta de la maquina: Piedra")
elif maquina ==1:
    print ("Apuesta de la maquina: Papel")
elif maquina==2:
    print ("Apuesta de la maquina: Tijera")
print ("Apuesta de la persona", persona)
match maquina:
    case 0: #piedra
        match persona:
            case "PIEDRA":
                print ("empate")
            case "PAPEL":
                print ("Gana la persona")
            case "TIJERA":
                print ("Gana la maquina")
            case _:
                print ("valor incorrecto")
    case 1: #papel   
        match persona:
            case "PIEDRA":
                print ("Gana la maquina")
            case "PAPEL":
                print ("Empate")
            case "TIJERA":
                print ("Gana la persona")
            case _:
                print ("valor incorrecto")
    case 2: #tijera
        match persona:
            case "PIEDRA":
                print ("Gana la persona")
            case "PAPEL":
                print ("Gana la maquina")
            case "TIJERA": 
                print ("Empate")
            case _:
                print ("valor incorrecto")
    case _:
        print ("valor incorrecto")