#Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
#una con los múltiplos de 5 y otra con el resto de los números.
# Imprimí ambas listas al finalizar.

lista_multiplos = []
otra_lista = []

numero = int(input("Ingrese un numero..."))

for i in range(1,numero+1):
    if i % 5 == 0:
        lista_multiplos.append(i)
    else:
        otra_lista.append(i)
        
for elemento in lista_multiplos:
    print(elemento)

for elemento in otra_lista:
    print(elemento)
    