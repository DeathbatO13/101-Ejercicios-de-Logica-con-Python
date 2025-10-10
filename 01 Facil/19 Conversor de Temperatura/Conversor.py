
def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convertir_fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

dato = float(input("Ingrese la temperatura a convertir: "))
unidad = input("Ingrese la unidad de la temperatura (°C para Celsius, °F para Fahrenheit): ").strip().upper()

if unidad == "°C":
    resultado = convertir_celsius_a_fahrenheit(dato)
    print(f"{dato}° Celsius son {resultado}° Fahrenheit.")
elif unidad == "°F":
    resultado = convertir_fahrenheit_a_celsius(dato)
    print(f"{dato}° Fahrenheit son {resultado}° Celsius.")
else:
    print("Error:Unidad no válida. Por favor ingrese '°C' o '°F'.")