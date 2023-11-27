Caracter= input ("Introduce un caracter" )
match Caracter:
    case "a" | "A":
        print ("Es la primera vocal ", Caracter)
    case "e" | "E":
        print ("Es la segunda vocal ", Caracter)
    case "i" | "I":
        print ("Es la tercera vocal ", Caracter)
    case "o" | "O":
        print ("Es la cuarta vocal ", Caracter)
    case "u" | "U":
        print ("Es la quinta vocal ", Caracter)
    case _:
        print ("No es una vocal")