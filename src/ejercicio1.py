################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados
y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados
en fahrenheit como un número decimal, utilice esta formula para calcular
los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""


def convertir_a_fahrrenheit(centigrados):
    """convertir_a_fahrrenheit(float) -> float
    Esta función toma como argumento un valor en
    grados centigrados y devuelve su equivalente en
    grados fahrenheit"""
    resultado = (centigrados * 9 / 5) + 32
    return resultado

def convertir_a_centigrados(fahrenheit):
    """convertir_a_centigrados(float) -> float
    Esta función toma como argumento un valor en
    grados fahrenheit y devuelve su equivalente en
    grados centigrados
    """
    resultado = (fahrenheit - 32) * 5 / 9
    return resultado

def principal():
    opcion = ""
    print("Para cambiar de centrigrados a fahrenheit presione c.\n")
    print("Para cambiar de fahrenheit a centigrados presione f.\n")
    while opcion != "c" and opcion != "f":
        opcion = input().lower()

    temperatura = int(input("Cuántos grados quiere convertir?: "))
    if opcion == "f":
        resultado = convertir_a_centigrados(temperatura)
    else:
        resultado = convertir_a_fahrrenheit(temperatura)
    print(f"El resultado de la conversión es: {resultado}")


if __name__ == "__main__":
    principal()
