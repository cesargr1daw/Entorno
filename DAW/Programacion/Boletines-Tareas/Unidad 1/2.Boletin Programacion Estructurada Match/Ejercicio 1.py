#Horario del dia
Dia= input ("Dia de la semana ").upper()
match Dia: 
    case "LUNES":
        print ("==========")
        print (  "LUNES")
        print ("==========")
        print ("8-9 FOL")
        print ("9-10 EDE")
        print ("10-11 PROG")
        print ("11-11:30 Recreo")
        print ("11:30-12 PROG")
        print ("12-14 BDD")
        print ("============")
    case "MARTES":
        print ("==========")
        print (  "MARTES")
        print ("==========")
        print ("8-9 FOL")
        print ("9-10 FOL")
        print ("10-11 SIS")
        print ("11-11:30 Recreo")
        print ("11:30-12 SIS")
        print ("12-14 LMSG")
        print ("============")
    case "MIERCOLES":
        print ("==========")
        print (  "MIERCOLES")
        print ("==========")
        print ("8-9 EDE")
        print ("9-10 EDE")
        print ("10-11 PROG")
        print ("11-11:30 Recreo")
        print ("11:30-12 PROG")
        print ("12-14 BDD")
        print ("============")
    case "JUEVES":
        print ("==========")
        print (  "JUEVES")
        print ("==========")
        print ("8-9 PROG")
        print ("9-10 PROG")
        print ("10-11 BDD")
        print ("11-11:30 Recreo")
        print ("11:30-12 BDD")
        print ("12-14 SIS")
        print ("============")
    case "VIERNES":
        print ("==========")
        print (  "VIERNES")
        print ("==========")
        print ("8-9 SIS")
        print ("9-10 SIS")
        print ("10-11 LMSG")
        print ("11-11:30 Recreo")
        print ("11:30-12 LMSG")
        print ("12-14 PROG")
        print ("============")
    case "SABADO":
        print ("Día de estudio y reflexión")
    case "DOMINGO":
        print ("Día de estudio y reflexión")
    case _:
        print ("Valor incorrecto")