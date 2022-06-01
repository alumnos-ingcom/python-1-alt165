################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos

Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""
def signo(numero):
    """signo(int)->int(-1|0|1)
    Esta función devuelve -1 si un número es negativo, 0 si es == 0 y 1 si es positivo
    """
    if numero == 0:
        return 0
    comparador = numero * numero
    comparador = comparador ** (0.5)#esta operación lo convierte en positivo al número
    resultado = numero - comparador
    if resultado == 0:
        return 1
    return -1

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    continuar = True
    while continuar:
        #este ciclo es para que solo se puedan ingresar valores numericos
        try:
            numero = int(input("Ingresar un número para devolver su signo:"))
            continuar = False
        except ValueError:
            print("No es un valor válido")

    resultado = signo(numero)
    print(resultado)

if __name__ == "__main__":
    principal()
    