################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos

Escribir una función que retorne una tuple con factores primos de un
numero entero positivo.

def factores_primos(numero):
"""
class NegativoExc(Exception):
    """Esta excepcion se lanza cuando el número es negativo"""

#from ejercicio8 import es_primo
try:
    from ejercicio8 import es_primo
except ImportError as exc:
    from src.ejercicio8 import es_primo

def es_multiplo(multiplo, divisor):
    """es_multiplo(int, int)-> boolean
    esta función devuelve true si un numero es divisor del otro
    """
    if multiplo % divisor == 0:
        return True
    return False

def factores_primos(numero):
    """factores_primos(int > 0) -> tuple
    Esta función toma un numero entero mayor a 0 y devuelve una tupla con los
    factores primos de ese número
    """
    if numero <= 0:
        return (0,)

    contador = 1
    tupla = ()
    while contador <= numero:
        if es_multiplo(numero, contador) and es_primo(contador):
            tupla_aux = (contador,)
            tupla = tupla + tupla_aux
        contador = contador + 1
    return tupla

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    continuar = True
    while continuar:
        try:
            numero = int(input("Ingrese el número para buscar sus factores primos: "))
            if numero < 0:
                raise NegativoExc
            continuar = False
        except ValueError:
            print("No es un valor válido")
        except  NegativoExc:
            print("El número tiene que ser positivo")

    resultado = factores_primos(numero)
    print(f"Los factores primos de {numero} son: {resultado}")

if __name__ == "__main__":
    principal()
