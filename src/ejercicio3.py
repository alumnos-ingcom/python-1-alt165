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
    continuar = True
    while continuar:
        try:
            numero1 = int(input("Ingrese el primer número: "))
            continuar = False
        except ValueError:
            print("No es un valor válido")

    continuar = True
    while continuar:
        try:
            numero2 = int(input("Ingrese el segundo número: "))
            continuar = False
        except ValueError:
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
