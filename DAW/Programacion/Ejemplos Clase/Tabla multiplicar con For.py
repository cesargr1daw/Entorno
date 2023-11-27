#Quiero que me lea por teclado un numero y nos de su tabla de multiplicar
multiplicar= int(input())
variable=0
for variableindice in range (1,11):
    variable=multiplicar*variableindice
    print (multiplicar,"x",variableindice, "=", variable)#Si sumamos 1 a variableindice y a variable eliminariamos 5x0