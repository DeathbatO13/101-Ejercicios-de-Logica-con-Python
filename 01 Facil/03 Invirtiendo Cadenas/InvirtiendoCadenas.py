## DeathbatO

cadena = input("Por favor ingrese la cadena a invertir: ")
print("Cadena inverida: ")
k = len(cadena)-1
cadenainvertida = ""

while k >= 0:
    cadenainvertida += cadena[k]
    k-=1
    
print(cadenainvertida)