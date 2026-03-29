#Dado un número N ingresado por el usuario
# imprima los números del 1 al N pero saltee los múltiplos de 5.
# Nota: utilizá la sentencia continue donde haga falta.

numero = int(input("Ingrese un numero..."))
i = 1
# for i in range(1,numero+1):
#    if i % 5 == 0:
#        continue
#    print(i)
    
# Misma consigna, pero usando while., pa' practicá' nomá'

while i <= numero:
    if i % 5 == 0:
        i+= 1
        continue
    print(i)
    i+=1

    