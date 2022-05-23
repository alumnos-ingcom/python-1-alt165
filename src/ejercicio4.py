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
    if numero > 0: #Esta rama es si numero es positivo
        while numero > 0:
            otro_numero = otro_numero + 1
            numero = numero - 1
    else: #Esta rama es cuando el primer número es negativo
        while numero < 0:
            otro_numero = otro_numero - 1
            numero = numero + 1

    return otro_numero

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = 5
    numero2 = -10
    resultado = suma_lenta(numero1, numero2)
    print(numero1, "+", numero2, "=", resultado)
    resultado = suma_lenta(numero2, numero1)
    print(numero2, "+", numero1, "=", resultado)

if __name__ == "__main__":
    principal()
