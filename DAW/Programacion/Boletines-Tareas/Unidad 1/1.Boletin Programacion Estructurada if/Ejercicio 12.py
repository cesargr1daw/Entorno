#Realizar un programa que lea el estado civil de una persona (S-Soltero, CCasado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por pantalla el porcentaje de retención que debe aplicarse de acuerdo con las siguientes reglas:
Estado=str(input("Estado Civil: ")).upper()
Edad=int (input ("Introducir la Edad"))
if Estado=="S"and Edad<35 or Estado=="D" and Edad<35:
    print ("12%")
elif Estado and Edad>50:
    print ("8.5%")
elif Estado=="V"and Edad<35 or "C" and Edad<35:
    print ("11.3%")
else:
    print ("10.5%")