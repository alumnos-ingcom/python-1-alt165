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
    if numero in (1, 2):
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
    continuar = True
    while continuar:
        try:
            numero = int(input("Ingrese el número para evaluar si es primo: "))
            continuar = False
        except ValueError:
            print("No es un valor válido")
    if es_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")

if __name__ == "__main__":
    principal()
