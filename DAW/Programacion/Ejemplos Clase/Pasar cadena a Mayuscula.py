Caracter= input ("Introduce un caracter" )
Caracter= Caracter.upper()
Caracter= Caracter.lower()
match Caracter:
    case "a" :
        print ("Es la primera vocal ", Caracter)
    case "e" :
        print ("Es la segunda vocal ", Caracter)
    case "i" :
        print ("Es la tercera vocal ", Caracter)
    case "o" :
        print ("Es la cuarta vocal ", Caracter)
    case "u" :
        print ("Es la quinta vocal ", Caracter)
    case _:
        print ("No es una vocal")
