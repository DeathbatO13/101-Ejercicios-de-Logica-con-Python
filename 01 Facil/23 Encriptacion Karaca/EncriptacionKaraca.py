def karaca_encrypt(texto):
    # 1. Revertir el texto
    texto = texto[::-1]
    # 2. Reemplazar vocales por números
    reemplazos = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'}
    texto = ''.join(reemplazos.get(c, c) for c in texto)
    # 3. Añadir "aca" al final
    return texto + "aca"

def karaca_decrypt(texto):
    # 1. Quitar "aca" del final
    if texto.endswith("aca"):
        texto = texto[:-3]
    # 2. Reemplazar números por vocales
    reemplazos = {'0': 'a', '1': 'e', '2': 'i', '3': 'o', '4': 'u'}
    texto = ''.join(reemplazos.get(c, c) for c in texto)
    # 3. Revertir el texto
    return texto[::-1]

# Ejemplo de uso

original = "encriptado con karaca"
encriptado = karaca_encrypt(original)
desencriptado = karaca_decrypt(encriptado)
print(f"Original: {original}")
print(f"Encriptado: {encriptado}")
print(f"Desencriptado: {desencriptado}")