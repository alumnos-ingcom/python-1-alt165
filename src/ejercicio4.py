################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Suma lenta

Escribir una función que haga la suma entre dos números enteros sin hacer la
operación de manera directa. Esto quiere decir que para hacer la suma entre
4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.

"""

def suma_lenta(numero, otro_numero):
    """suma_lenta(int, int) -> int
        esta función devuelve el resultado de la suma de dos enteros
    """
    if numero > 0:
        while numero > 0:
            otro_numero = otro_numero + 1
            numero = numero - 1
    else:
        while numero < 0:
            otro_numero = otro_numero - 1
            numero = numero + 1
    
    return otro_numero
        
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    pass

if __name__ == "__main__":
    principal()

