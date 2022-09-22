# ------------------------------------------------------
# Convierte un número binario a hexadecimal.
# El número binario es un string e.g. "101"
# El número hexadecimal es también un string e.g. "AB5"
# ------------------------------------------------------

def TablabinHex(cuatro_digitos_binarios):
    digito_hexadecimal = ""
    if cuatro_digitos_binarios == "0000":
        digito_hexadecimal = "0"
    elif cuatro_digitos_binarios == "0001":
        digito_hexadecimal = "1"
    elif cuatro_digitos_binarios == "0010":
        digito_hexadecimal = "2"
    elif cuatro_digitos_binarios == "0011":
        digito_hexadecimal = "3"
    elif cuatro_digitos_binarios == "0100":
        digito_hexadecimal = "4"
    elif cuatro_digitos_binarios == "0101":
        digito_hexadecimal = "5"
    elif cuatro_digitos_binarios == "0110":
        digito_hexadecimal = "6"
    elif cuatro_digitos_binarios == "0111":
        digito_hexadecimal = "7"
    elif cuatro_digitos_binarios == "1000":
        digito_hexadecimal = "8"
    elif cuatro_digitos_binarios == "1001":
        digito_hexadecimal = "9"
    elif cuatro_digitos_binarios == "1010":
        digito_hexadecimal = "A"
    elif cuatro_digitos_binarios == "1011":
        digito_hexadecimal = "B"
    elif cuatro_digitos_binarios == "1100":
        digito_hexadecimal = "C"
    elif cuatro_digitos_binarios == "1101":
        digito_hexadecimal = "D"
    elif cuatro_digitos_binarios == "1110":
        digito_hexadecimal = "E"
    elif cuatro_digitos_binarios == "1111":
        digito_hexadecimal = "F"
    return digito_hexadecimal

def bin2hex(numero_binario):
    n = numero_binario

    while len(n)%4 != 0:
        n = "0" + n

    numero_hexadecimal = ""
    for i in range(int(len(n)/4)):
        numero_hexadecimal += TablabinHex(n[i*4:i*4+4])
        
    return numero_hexadecimal

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":
    # Pide al usuario el número binario a convertir 
    # Como el número binario es un string, no hace falta usar int()
    numero_binario = input("Escribe el número en binario que quieres convertir: ")

    # se llama a la función bin2hex() para hacer la conversión
    numero_hexadecimal = bin2hex(numero_binario)

    # Muestra por pantalla el resultado.
    print("El numero binario " + numero_binario + " es " + numero_hexadecimal + " en hexadecimal.")
