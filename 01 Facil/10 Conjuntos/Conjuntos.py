## DeathbatO

def encontrar_elementos(array1, array2, buscar_comunes):
    if buscar_comunes:
        conjunto1 = set(array1)
        conjunto2 = set(array2)
        elementos_comunes = list(conjunto1.intersection(conjunto2))
        return elementos_comunes
    else:
        conjunto1 = set(array1)
        conjunto2 = set(array2)
        elementos_no_comunes = list(conjunto1.symmetric_difference(conjunto2))
        return elementos_no_comunes


array1_input = input("Ingrese los elementos del primer array separados por comas: ")
array2_input = input("Ingrese los elementos del segundo array separados por comas: ")

array1 = [int(x) for x in array1_input.split(",")]
array2 = [int(x) for x in array2_input.split(",")]
comunes_input = input("¿Desea buscar elementos comunes? (s/n): ")
comunes = comunes_input.lower() == 's'
resultado = encontrar_elementos(array1, array2, comunes)
print("Resultado:", resultado)