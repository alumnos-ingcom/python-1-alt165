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

def ordenar_mayor_a_menor(uno, dos, tres):
    """ordenar_mayor_a_menor(int|float,int|float,int|float)->tupla(numero,numero,numero)
    esta funcion toma tres valores y los devuelve ordenados de mayor a menor
    """
    if uno < dos:
        uno, dos = dos, uno
    if uno < tres:
        uno, tres = tres, uno
    if dos < tres:
        dos, tres = tres, dos
    return uno, dos, tres

def ordenar_menor_a_mayor(uno, dos, tres):
    """ordenar_menor_a_mayor(int|float,int|float,int|float)->tupla(numero,numero,numero)
    esta funcion toma tres valores y los devuelve ordenados de menor a mayor
    """
    if uno > dos:
        uno, dos = dos, uno
    if uno > tres:
        uno, tres = tres, uno
    if dos > tres:
        dos, tres = tres, dos
    return uno, dos, tres

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    continuar = True
    while continuar:#verifica que solo se ingresen numeros
        try:
            numero1 = int(input("Ingrese el primer número: "))
            continuar = False
        except ValueError:
            print("No es un valor válido")

    continuar = True
    while continuar:#verifica que solo se ingresen numeros
        try:
            numero2 = int(input("Ingrese el segundo número: "))
            continuar = False
        except ValueError:
            print("No es un valor válido")

    continuar = True
    while continuar:#verifica que solo se ingresen numeros
        try:
            numero3 = int(input("Ingrese el tercer número: "))
            continuar = False
        except ValueError:
            print("No es un valor válido")

    print("Los valores ordenados son:")
    print("De mayor a menor")
    print(ordenar_mayor_a_menor(numero1, numero2, numero3))
    print("De menor a mayor")
    print(ordenar_menor_a_mayor(numero1, numero2, numero3))

if __name__ == "__main__":
    principal()
