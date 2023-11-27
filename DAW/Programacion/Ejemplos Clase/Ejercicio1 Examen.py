sheldon=str(input("Introduce tu elección Sheldon")).upper()
persona=str(input("Introduce tu elección"))
match sheldon:
    case "PIEDRA":
        match persona:
            case "PIEDRA":
                print ("Sheldon y tu habeis empatado")
            case "TIJERA":
                print ("Sheldon Gana")
            case "PAPEL":
                print("Sheldon Pierde")
            case "LAGARTO":
                print ("Sheldon Gana")
            case "SPOCK":
                print ("Sheldon Pierde")
    case "PAPEL":
        match persona:
            case "PIEDRA":
                print ("Sheldon Gana")
            case "TIJERA":
                print ("Sheldon Pierde")
            case "PAPEL":
                print("Sheldon y tu habeis empatado")
            case "LAGARTO":
                print ("Sheldon Pierde")
            case "SPOCK":
                print ("Sheldon Gana")
    case "TIJERA":
        match persona:
            case "PIEDRA":
                print ("Sheldon Pierde")
            case "TIJERA":
                print ("Sheldon y tu habeis empatado")
            case "PAPEL":
                print("Sheldon Gana")
            case "LAGARTO":
                print ("Sheldon Gana")
            case "SPOCK":
                print ("Sheldon Pierde")
    case "LAGARTO":
        match persona:
            case "PIEDRA":
                print ("Sheldon Pierde")
            case "PAPEL":
                print("Sheldon Gana")
            case "TIJERA":
                print("Sheldon Pierde")
            case "LAGARTO":
                print("Sheldon y tu habeis empatado")
            case "SPOCK":
                print("Sheldon Gana")
    case "SPOCK":
        match persona:
            case "PIEDRA":
                print("Sheldon Gana")
            case "PAPEL":
                print("Sheldon Pierde")
            case "TIJERA":
                print("Sheldon Gana")
            case "LAGARTO":
                print("Sheldon Pierde")
            case "SPOCK":
                print("Sheldon y tu habeis empatado")
                