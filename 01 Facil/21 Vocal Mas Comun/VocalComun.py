
texto = input("Ingrese un texto: ")

vocales = "aeiou"
contador = {vocal: 0 for vocal in vocales}


if any(vocal in texto for vocal in vocales):
    for letra in texto.lower():
        if letra in contador:
            contador[letra] += 1
else:
    print("No hay vocales en el texto.")
    exit()

vocal_mas_comun = max(contador, key=contador.get)
print("La vocal más común es:", vocal_mas_comun)