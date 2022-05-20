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
    if numero >= 0:
        return numero
    else:
        return numero * (-1)

def compara(numero, otro_numero):
    """compara(int|float, int|float)-> int(1|-1|0)"""
    resto = numero - otro_numero
    if resto != 0:
        return resto / absoluto(resto)
    else:
        return resto
    
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    pass

if __name__ == "__main__":
    principal()

