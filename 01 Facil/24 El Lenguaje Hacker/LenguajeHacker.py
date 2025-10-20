#DeathbatO

lenguaje_hacker = {
    'A': '4', 'B': '8', 'C': '<', 'D': ')', 'E': '£', 'F': '|=', 'G': '<-',
    'H': '#', 'I': '1', 'J': '_|', 'K': '|<', 'L': '1_', 'M': r'|\/|',  # Corregido
    'N': r'|\|', 'O': '0', 'P': '|*', 'Q': '(_,)', 'R': '|2', 'S': '5',  # Corregido
    'T': '7', 'U': '|_|', 'V': r'\/', 'W': r'\/\/', 'X': '}{', 'Y': '`/', # Corregidos
    'Z': '2'
}

def traducir_a_lenguaje_hacker(texto):
    texto = texto.upper()
    traduccion = ''
    for caracter in texto:
        if caracter in lenguaje_hacker:
            traduccion += lenguaje_hacker[caracter]
        else:
            traduccion += caracter
    return traduccion

texto = input("Ingrese el texto a traducir a lenguaje hacker: ")
texto_traducido = traducir_a_lenguaje_hacker(texto)
print("Texto traducido a lenguaje hacker:", texto_traducido)