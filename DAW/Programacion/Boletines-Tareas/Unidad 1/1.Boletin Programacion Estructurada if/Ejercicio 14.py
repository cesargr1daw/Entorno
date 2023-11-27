#14.Escribe un programa que tome la calificación de un examen como entrada y muestre la calificación equivalente en letras (A, B, C, D o F) según la siguiente escala: 90-100 A, 80-89 B, 70-79 C, 60-69 D, por debajo de 60 F.
Calificacion=int(input("Introduce la calificación:"))
if Calificacion==100 and Calificacion>=90:
    print ("A")
elif Calificacion<=89 and Calificacion>=80:
    print ("B")
elif Calificacion<=79 and Calificacion>=70:
    print ("C")
elif Calificacion<=69 and Calificacion>=60:
    print ("D")
elif Calificacion<=59 and Calificacion>=0:
    print ("F")