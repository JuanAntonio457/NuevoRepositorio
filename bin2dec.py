# ------------------------------------------------------
# Convierte un número decimal positivo a binario usando un 
#   determinado número de bits.
# El binario resultante es un string e.g. "101"
# Se usa la función bin() que transforma e.g. 3 en "0b11".
# En esta función se quita el "0b" para dejar el "11"
# ------------------------------------------------------
def dec2bin(numero_decimal, numero_bits):
    numero_binario = bin(numero_decimal)
    if numero_decimal >= 0:
        numero_binario = numero_binario[2:len(numero_binario)]  # quita el "0b" del principio

        while len(numero_binario) < numero_bits:      # añade 0's a la izquierda si hace falta
            numero_binario = "0" + numero_binario
    else:
        numero_binario = numero_binario[3:len(numero_binario)]  # quita el "-0b" del principio

        while len(numero_binario) < numero_bits:      # añade 1's a la izquierda si hace falta
            numero_binario = "1" + numero_binario

    return numero_binario

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":
    # Pide al usuario el número a convertir y el número de bits 
    # Como el resultado de input es de tipo string, se convierte a entero usando int()
    numero_decimal = int(input("Escribe el número en decimal que quieres convertir: "))
    numero_bits = int(input("Cuantos bits tendrá el número binario: "))

    # se llama a la función dec2bin() para hacer la conversión
    numero_binario = dec2bin(numero_decimal, numero_bits)

    # Muestra por pantalla el resultado.
    # Para imprimir un entero es necesario convertirlo a string con str()
    print("El numero " + str(numero_decimal) + " es " + numero_binario + " en binario con " + str(numero_bits) + " bits.")
