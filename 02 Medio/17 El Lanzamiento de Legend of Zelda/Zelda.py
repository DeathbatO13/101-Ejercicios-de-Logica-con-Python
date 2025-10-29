#DeathbatO

from datetime import date

# Diccionario con algunos juegos de The Legend of Zelda y sus fechas de lanzamiento
zelda_games = {
    "The Legend of Zelda": date(1986, 2, 21),
    "Zelda II: The Adventure of Link": date(1987, 1, 14),
    "The Legend of Zelda: A Link to the Past": date(1991, 11, 21),
    "The Legend of Zelda: Ocarina of Time": date(1998, 11, 21),
    "The Legend of Zelda: Majora's Mask": date(2000, 4, 27),
    "The Legend of Zelda: The Wind Waker": date(2002, 12, 13),
    "The Legend of Zelda: Twilight Princess": date(2006, 11, 19),
    "The Legend of Zelda: Skyward Sword": date(2011, 11, 18),
    "The Legend of Zelda: Breath of the Wild": date(2017, 3, 3),
    "The Legend of Zelda: Tears of the Kingdom": date(2023, 5, 12)
}

print("Lista de juegos disponibles:")
for title in zelda_games:
    print(f"- {title}")

# Solicitar los juegos al usuario
game1 = input("\nIngresa el primer juego: ").strip()
game2 = input("Ingresa el segundo juego: ").strip()

# Verificar si los títulos existen en el diccionario
if game1 not in zelda_games or game2 not in zelda_games:
    print("\n Uno o ambos títulos no están en la lista.")
else:
    # Calcular la diferencia
    date1 = zelda_games[game1]
    date2 = zelda_games[game2]
    diff = abs(date2 - date1)

    # Convertir días a años aproximados
    years = diff.days // 365
    days = diff.days % 365

    print(f"\nEntre '{game1}' ({date1}) y '{game2}' ({date2}) han pasado aproximadamente:")
    print(f" {years} años y {days} días ({diff.days} días en total).")