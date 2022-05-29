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
    numero1 = ""
    numero2 = ""
    numero3 = ""
    while not isinstance(numero1, int):#verifica que solo se ingresen numeros
        numero1 = input("Ingrese el primer número: ")
        if numero1.lstrip("-").isdecimal():
            numero1 = int(numero1)
        else:
            print("No es un valor válido")

    while not isinstance(numero2, int):#verifica que solo se ingresen numeros
        numero2 = input("Ingrese el segundo número: ")
        if numero2.lstrip("-").isdecimal():
            numero2 = int(numero2)
        else:
            print("No es un valor válido")

    while not isinstance(numero3, int):#verifica que solo se ingresen numeros
        numero3 = input("Ingrese el tercer número: ")
        if numero3.lstrip("-").isdecimal():
            numero3 = int(numero3)
        else:
            print("No es un valor válido")

    print("Los valores ordenados son:")
    print("De mayor a menor")
    print(ordenar_mayor_a_menor(numero1, numero2, numero3))
    print("De menor a mayor")
    print(ordenar_menor_a_mayor(numero1, numero2, numero3))

if __name__ == "__main__":
    principal()
