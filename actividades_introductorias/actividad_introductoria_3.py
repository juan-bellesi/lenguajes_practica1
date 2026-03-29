#Crea un programa que solicite al usuario un número
# y muestre su tabla de multiplicar del 1 al 10 utilizando un bucle for.
factores = [1,2,3,4,5,6,7,8,9,10]

numero = int(input("Ingrese un numero entero..."))
print(f"El numero ingresado es {numero}.")

for factor in factores:
    multiplicacion = numero * factor
    print (multiplicacion)
    
    
    
