def es_numero_perfecto(numero):
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor
    return suma_divisores == numero


numero = 5
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto")
else:
    print(f"{numero} no es un número perfecto")
