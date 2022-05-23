################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Números primos

Escribir una función que indique con True si un numero indicado es Primo.

"""
def es_primo(numero):
    """es_primo(int > 0)-> boolean
    esta función devuelve True si un numero es primo,
    si no lo es devuelve False
    """
    if numero <= 0:
        return False

    es_primo_flag = True
    if numero == 1 or numero == 2:
        return True

    if numero % 2 == 0:
        es_primo_flag = False
        return es_primo_flag

    mitad = numero // 2 #solo es necesario buscar divisores hasta la primer mitad del numero
    contador = 3

    while contador <= mitad:
        if numero % contador == 0:
            es_primo_flag = False
            return es_primo_flag
        contador = contador + 2 #solo es necesario comparar contra numeros impares

    return es_primo_flag

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    desde = 1
    hasta = 200
    while desde < hasta:
        print(desde)
        if es_primo(desde):
            print(" es primo\n")
        else:
            print(" no es primo\n")
        desde = desde + 1

if __name__ == "__main__":
    principal()
