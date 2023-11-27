numE=int (input("Numero de empleados"))
mediaedadjava=0
mediaedadpython=0
numEMujerjava=0
numEHombrejava=0
numEMujerpython=0
numEHombrepython=0
NumeroJava=0
Numeropython=0
for i in range (0,numE):
    edadEmpleado=int (input("Edad"))
    genero=input ("genero").upper()
    while not (edadEmpleado <=65 and edadEmpleado>=18):
        edadEmpleado = int (input("Edad"))
    lenguaje=input ("Introduce lenguaje").upper()
    match lenguaje:
        case "JAVA":
            NumeroJava=NumeroJava+1
            mediaedadjava=mediaedadjava+edadEmpleado
            match genero:
                case "HOMBRE":
                    numEHombrejava=numEHombrejava+1
                case "MUJER":
                    numEMujerjava=numEMujerjava+1
        case "PYTHON":
            #to do
            print ("Completa")        
mediaedadjava=mediaedadjava/NumeroJava
mediaedadpython=mediaedadpython/Numeropython
print("El.....")
print("El.....")