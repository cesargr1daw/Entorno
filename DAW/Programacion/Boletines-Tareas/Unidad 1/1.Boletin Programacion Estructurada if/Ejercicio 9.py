#Ejercicio 9 Realizar un programa que lea la edad de una persona menor a 100 años einforme de si es un niño (0-12 años), un adolescente (13-17), un joven (18-29) o un adulto.
Años=int (input ("Años"))
if Años<100:
    if Años>=0 and Años<=12:
        print ("Es un niño")
    else:
        if Años>=13 and Años<=17:
            print ("Es un adolescente")
        else:
            if Años>=18 and Años<=29:
                print ("Es un joven")
            else:
                Años>=30 and Años<=99
                print ("Es un Adulto")