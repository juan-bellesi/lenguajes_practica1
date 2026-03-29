#Escribe un programa que simule una caja registradora:
# el usuario ingresa precios de productos de a uno.
# Cuando ingresa 0, el programa se detiene y muestra el total acumulado.
# Nota: utilizá la sentencia break cuando haga falta.

sumatoria = 0

precio = float(input("Ingrese el precio del producto y escriba 0 cuando quiera dar por terminada la suma: "))

while precio != 0:
    sumatoria = sumatoria + precio
    precio = float(input("Ingrese otro precio. Recuerde usar cero para finalizar: "))

print(f"El precio total de los productos ingresados es {sumatoria} pesos")