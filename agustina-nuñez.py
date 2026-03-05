import random

palabras = ["python", "computadora", "programacion", "juego", "algoritmo"]
palabra = random.choice(palabras)

vidas = 6
letras_correctas = []
letras_incorrectas = []

def mostrar_palabra(palabra, letras_correctas):
    resultado = ""
    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra
        else:
            resultado += "_ "
    return resultado

while vidas > 0:
    print("\nPalabra:", mostrar_palabra(palabra, letras_correctas))
    print("Vidas:", vidas)
    print("Letras incorrectas:", letras_incorrectas)

    letra = input("Ingresá una letra (o escribí 'salir' para terminar): ").lower()

    if letra == "salir":
        print("Terminaste el juego.")
        break

    if not letra.isalpha() or len(letra) != 1:
        print("Por favor ingresá solo una letra.")
        continue

    if letra in palabra:
        if letra not in letras_correctas:
            letras_correctas.append(letra)
            print("¡Bien! Letra correcta.")
    else:
        if letra not in letras_incorrectas:
            letras_incorrectas.append(letra)
            vidas -= 1
            print("Letra incorrecta.")

    if all(letra in letras_correctas for letra in palabra):
        print("\n¡FELICITACIONES! Adivinaste la palabra:", palabra)
        break

if vidas == 0:
    print("\nPerdiste 😢 La palabra era:", palabra)