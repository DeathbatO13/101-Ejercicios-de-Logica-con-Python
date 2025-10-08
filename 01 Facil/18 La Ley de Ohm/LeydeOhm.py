# DeathbatO

def calcular_ley_ohm(voltaje=None, corriente=None, resistencia=None):
    if voltaje is not None:
        if corriente is not None:
            resistencia = voltaje / corriente
            return f"La resistencia es: {resistencia:.2f} ohmios"
        elif resistencia is not None:
            corriente = voltaje / resistencia
            return f"La corriente es: {corriente:.2f} amperios"
        else:
            return "Invalid values."
    elif corriente is not None:
        if resistencia is not None:
            voltaje = corriente * resistencia
            return f"El voltaje es: {voltaje:.2f} voltios"
        else:
            return "Invalid values"
    elif resistencia is not None:
        return "Invalid values"
    else:
        return "Invalid values"
    
# --- Entrada del usuario ---
def leer_valor(mensaje):
    valor = input(mensaje)
    return float(valor) if valor.strip() != "" else None

voltaje = leer_valor("Ingrese el voltaje (V) o deje en blanco: ")
corriente = leer_valor("Ingrese la corriente (I) o deje en blanco: ")
resistencia = leer_valor("Ingrese la resistencia (R) o deje en blanco: ")

resultado = calcular_ley_ohm(voltaje, corriente, resistencia)
print(resultado)