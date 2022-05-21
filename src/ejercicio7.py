################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Transformación de un número

Escribir un programa que permita transformar un número solicitado
expresado en grados, minutos y segundos a segundos a segundos.
Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.

"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    """sexadecimal_a_decimal(horas int, minutos int, segundos int) -> int
    esta función toma tres valores expresados en grados minutos y segundos
    y devuelve el valor expresado en segundos
    
    """
    return (horas*3600+ minutos * 60 + segundos)

def decimal_a_sexadecimal(numero):
    horas = numero // 3600
    numero = numero % 3600
    minutos = numero // 60
    segundos = numero % 60
    return horas, minutos, segundos

    
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    #print(sexadecimal_a_decimal(1,1,1))
    #print(decimal_a_sexadecimal(sexadecimal_a_decimal(2,2,2)))
    pass

if __name__ == "__main__":
    principal()

