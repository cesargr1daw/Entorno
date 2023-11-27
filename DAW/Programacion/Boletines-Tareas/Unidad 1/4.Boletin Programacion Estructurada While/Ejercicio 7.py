#Crea un programa que seleccione un número aleatorio y el usuario debe adivinarlo. El bucle while se ejecuta hasta que el usuario adivine
#correctamente.
import random
maquina=random.randint(0,10)
persona=int (input("Dime que numero ha pensado la maquina:"))
while maquina!=persona:
    persona=int(input("Dime que numero ha pensado la maquina"))
print("Has acertado, era el ", maquina)