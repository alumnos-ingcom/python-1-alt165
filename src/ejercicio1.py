################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Enunciado del ejercicio
"""
# Reemplazar por las funciones del ejercicio

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
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    pass

if __name__ == "__main__":
    principal()

