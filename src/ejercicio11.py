################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de

Escribir una función que indique con True si un número entero es multiplo
de otro, utilizando sumas y restas.

"""
class NegativoExc(Exception):
    """Esta exepcion se levanta si un valor es negativo"""

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
    continuar = True
    while continuar:
        try:
            numero = int(input("Ingrese el primer número:"))
            if numero < 0:
                raise NegativoExc
            continuar = False
        except ValueError:
            print("No es un valor válido")
        except NegativoExc:
            print("Ingrese un valor positivo")

    continuar = True
    while continuar:
        try:
            posible_multiplo = int(input("Ingrese el posible múltiplo:"))
            if posible_multiplo < 0:
                raise NegativoExc
            continuar = False
        except ValueError:
            print("No es un valor válido")
        except NegativoExc:
            print("Ingrese un valor positivo")

    if es_multiplo(numero, posible_multiplo):
        print(f"{posible_multiplo} es múltiplo de  {numero}")
    else:
        print(f"{posible_multiplo} no es múltiplo de  {numero}")

if __name__ == "__main__":
    principal()
