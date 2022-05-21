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
def es_primo(numero):
    """es_primo(int > 0)-> boolean
    esta función devuelve True si un numero es primo,
    si no lo es devuelve False
    """
    if numero <= 0:
        return False

    es_primo_flag = True

    if numero == 1 or numero == 2:
        return es_primo_flag

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
    else:
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
    print(factores_primos(110))
   
if __name__ == "__main__":
    principal()
