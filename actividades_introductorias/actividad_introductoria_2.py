#Escribe un programa que solicite al usuario una cantidad de segundos
# y muestre cuántas horas, minutos y segundos equivalen.
# Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.

segundos = int(input("Ingrese la cantidad de segundos que quiera: "))

print(f"Usted ingresó {segundos}")

horas = segundos // 3600

print (f"la cantidad de horas es {horas}")

segundos_restantes = segundos % 3600

print (f"la cantidad de horas es {horas} y te sobraron {segundos_restantes} segundos")

minutos = segundos_restantes // 60

print (f"La cantidad de minutos es {minutos}")

