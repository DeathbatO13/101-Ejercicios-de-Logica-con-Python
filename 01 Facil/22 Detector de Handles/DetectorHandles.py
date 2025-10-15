# DeathbatO13

import re

def detectar_handles(texto):
    
    usuarios = re.findall(r'@\w+', texto)
    
    hashtags = re.findall(r'#\w+', texto)
    
    webs = re.findall(r'(?:https?://|www\.)[^\s]+?\.(?:com|es|net|org|edu|gov|info|io|co)', texto)
    return {
        'usuarios': usuarios,
        'hashtags': hashtags,
        'webs': webs
    }

# Ejemplo de uso
if __name__ == "__main__":
    texto = "Sígueme en @Daniel y usa #Python. Visita https://github.com/DeathbatO13 o www.ejemplo.es para más info."
    print("Texto de ejemplo:")
    print(texto)
    print("\nResultados del detector de handles:")
    print(detectar_handles(texto))