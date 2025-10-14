
# DeathbatO

def esBoomerang(p1, p2, p3):
    return (p1 == p3 and p1 != p2)

arregloejemplo1 = [2, 1, 2, 3, 3, 4, 2, 4, 2]
arregloejemplo2 = [1, 2, 3, 4, 3]

print("Arreglo Ejemplo 1:", arregloejemplo1)
print("Arreglo Ejemplo 2:", arregloejemplo2)

for i in range(len(arregloejemplo1) - 2):
    if esBoomerang(arregloejemplo1[i], arregloejemplo1[i+1], arregloejemplo1[i+2]):
        print("El arreglo ejemplo 1 tiene un bumeran en la posicion:", i, "con los valores:", arregloejemplo1[i:i+3])

for i in range(len(arregloejemplo2) - 2):
    if esBoomerang(arregloejemplo2[i], arregloejemplo2[i+1], arregloejemplo2[i+2]):
        print("El arreglo ejemplo 2 tiene un bumeran en la posicion:", i, "con los valores:", arregloejemplo2[i:i+3])