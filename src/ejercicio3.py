################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Comparación de números

Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

    Retornar -1 si el primero es menor que el segundo
    Retornar 0 si son iguales
    Retornar 1 si el primero es mayor que el segundo

"""

def absoluto(numero):
    """absoluto(int)->int
    Esta función devuelve el valor absoluto de un numero"""
    if numero < 0:
        numero = numero * (-1)
    return numero

def compara(numero, otro_numero):
    """compara(int|float, int|float)-> int(1|-1|0)"""
    resto = numero - otro_numero
    if resto != 0:
        resto = resto / absoluto(resto)
    resto = int(resto)
    return resto

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = ""
    numero2 = ""
    while not isinstance(numero1, int):
        numero1 = input("Ingrese el primer número: ")
        if numero1.lstrip("-").isdecimal():
            numero1 = int(numero1)
        else:
            print("No es un valor válido")

    while not isinstance(numero2, int):
        numero2 = input("Ingrese el segundo número: ")
        if numero2.lstrip("-").isdecimal():
            numero2 = int(numero2)
        else:
            print("No es un valor válido")

    comparador = compara(numero1, numero2)
    if comparador > 0:
        print(f"{numero1} es mayor que {numero2}")
    elif comparador < 0:
        print(f"{numero1} es menor que {numero2}")
    else:
        print(f"{numero1} y {numero2} son iguales")

if __name__ == "__main__":
    principal()
