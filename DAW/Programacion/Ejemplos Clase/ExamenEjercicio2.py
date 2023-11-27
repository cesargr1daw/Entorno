opcionmenu=0
totalalumnosEntran=0
while opcionmenu!=4:
    print("#####################################################")
    print("# Bienvenido al IES Jacarandá!!:                    #")
    print("     1.  Alumnos que han entrado:")
    print("     2.  Alumnos que han abandonado el centro:")
    print("     3.  Alumnos en el IES:")
    print("     4.  Salir")
    print("#####################################################")
    opcionmenu=int (input("Introduce la opción:"))
    if opcionmenu==1:
        #alumnoscentro=int(input("Alumnos que entran el el centro:"))
        totalalumnosEntran+=    int (input("Introduce la opción:"))
       # totalalumnosEntran=alumnoscentro+totalalumnosEntran
        
    elif opcionmenu==2:
              totalalumnosEntran-=    int (input("Introduce la opción:"))
    
    elif opcionmenu==3:
        print (totalalumnosEntran)
   
    elif 4:
        print ("Cerrar programa")
    