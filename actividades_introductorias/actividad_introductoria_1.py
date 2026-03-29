#Escribe un programa que solicite al usuario su año de nacimiento
# y muestre en qué año cumplirá 18, 21 y 100 años.

nacimiento = int(input("Ingrese su año de nacimiento..."))
mayoria = nacimiento + 18
veintena = nacimiento + 21
centenario = nacimiento + 100
print(f"Usted va a cumplir 18 años en {mayoria}")
print(f"Usted va a cumplir 21 años en {veintena}")
print(f"Usted va a cumplir 100 años en {centenario}")