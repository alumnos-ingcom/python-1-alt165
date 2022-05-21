################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de

Escribir una función que indique con True si un número entero es multiplo
de otro, utilizando sumas y restas.

"""
def es_multiplo(numero, multiplo):
    """es_multiplo(int,int)-> boolean
    esta función devuelve True si multiplo es multiplo de numero,
    devuelve False si no lo es
    """
    while multiplo >= numero:
        multiplo = multiplo - numero

    if multiplo != 0:
        return False

    return True

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print(es_multiplo(10,205))
if __name__ == "__main__":
    principal()
