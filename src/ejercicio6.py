################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Ordenar 3 valores

Escribir una función que a partir de tres variables de tipo entero
retorne una tupla con dichos valores ordenados de menor a mayor.
Y Viceversa

"""
def swap(uno, dos):
    """swap(int|float,int|float)->int|float,int|float
    esta funcion toma dos valores y los devuelve intercambiados
    """
    uno, dos = dos, uno
    return uno, dos


def ordenar_mayor_a_menor(uno, dos, tres):
    """ordenar_mayor_a_menor(int|float,int|float,int|float)->tupla(numero,numero,numero)
    esta funcion toma tres valores y los devuelve ordenados de mayor a menor
    """
    if uno < dos:
        uno, dos = swap(uno, dos)
    if uno < tres:
        uno, tres = swap(uno, tres)
    if dos < tres:
        dos, tres = swap(dos, tres)
    return uno, dos, tres

def ordenar_menor_a_mayor(uno, dos, tres):
    """ordenar_menor_a_mayor(int|float,int|float,int|float)->tupla(numero,numero,numero)
    esta funcion toma tres valores y los devuelve ordenados de menor a mayor
    """
    if uno > dos:
        uno, dos = swap(uno, dos)
    if uno > tres:
        uno, tres = swap(uno, tres)
    if dos > tres:
        dos, tres = swap(dos, tres)
    return uno, dos, tres

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))
    print("Los valores ordenados son:\n")
    print(ordenar_mayor_a_menor(numero1, numero2, numero3))
    print(ordenar_menor_a_mayor(numero1, numero2, numero3))

if __name__ == "__main__":
    principal()
