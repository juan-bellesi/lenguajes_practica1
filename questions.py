import random

categorias = {
    "programacion": ["python", "variable", "funcion", "bucle"],
    "tipos": ["cadena", "entero", "lista"],
    "general": ["programa"]
}

print("Categorías disponibles:")
for categoria in categorias:
    print("-", categoria)

# Elegir categoría correctamente
while True:
    categoria_elegida = input("Elegí una categoría: ")
    if categoria_elegida in categorias:
        break
    else:
        print("Categoría no válida")

# Recién acá elegimos la palabra
word = random.choice(categorias[categoria_elegida])

guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    if "_" not in progress:
        puntaje += 6
        print("¡Ganaste!")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Entrada no válida")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1
        print("Esa letra no está en la palabra.")

    print()

else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word}")

print(f"Puntaje final: {puntaje}")