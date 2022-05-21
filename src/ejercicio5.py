################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Divisiones

Escribir una función que mediante restas sucesivas,
obtenga el valor del cociente y resto de dos números enteros.

"""

def division_lenta(dividendo, divisor):
    """
    division_lenta(int, int != 0) -> (int,int)
    Esta función devuelve el resultado y el resto de la division
    entera entre dos numeros con el divisor != 0
    devuelve (0, 0) si se le pasan valores negativos o el divisor es 0
    """
    if divisor == 0:
        return 0, 0
    if (divisor < 0 or dividendo < 0):
        return 0, 0
    
    cociente = 0
    
    resto = dividendo
    
    while resto >= divisor:
        resto = resto - divisor
        cociente = cociente + 1
            
    return cociente, resto
        
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    pass

if __name__ == "__main__":
    principal()

