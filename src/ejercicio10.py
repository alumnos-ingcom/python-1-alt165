################
# José Lambrechts - @alt165
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o
frase ingresada se trata de un palindromo. Palíndromo, es si
se lee igual de derecha a izquierda que de izquierda a derecha.
"""
def invertir_str(string):
    """
    invertir_str(string)-> string
    esta funcion toma un string y devuelve otro string con los
    carácteres invertidos.
    """
    invertido = ""
    for element in string:
        invertido = element + invertido
    return invertido

def es_palindromo(texto):
    """
    es_palindromo(string) -> boolean
    esta función devuelve True si un string es palíndromo,
    devuelve False si no lo es
    """
    texto = texto.lower()
    return texto == invertir_str(texto)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    entrada = input("Ingresar el texto a verificar: ")
    if es_palindromo(entrada):
        print("el texto es palindromo")
    else:
        print("El texto no es palindromo")

if __name__ == "__main__":
    principal()
