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
class MayorASesenta(Exception):
    """Esta excepcion se lanza cuando el valor es > 60
    """


class Negativo(Exception):
    """Esta excepcion se lanza cuando el número es negativo"""


def sexadecimal_a_decimal(horas, minutos, segundos):
    """sexadecimal_a_decimal(horas int, minutos int < 60, segundos int < 60) -> int
    esta función toma tres valores expresados en grados minutos y segundos
    y devuelve el valor expresado en segundos
    """
    total = horas * 3600 + minutos * 60 + segundos
    return total

def decimal_a_sexadecimal(numero):
    """decimal_a_sexadecimal(int) -> tuple(int, int < 60, int < 60)
    """
    #hay que limitar la entrada para que no acepte segundos y minutos > 60
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
    opcion = ""

    print("Para convertir de sexadecimal a decimal presione S")
    print("Para convertir de decimal a sexadecimal presione D")
    while opcion not in ("d", "D", "s", "S"):
        opcion = input()

    if opcion in ("d", "D"):
        continuar = True
        while continuar:
            try:
                decimal = int(input("Cuál es valor a convertir?: "))
                continuar = False
            except ValueError:
                print("No es un valor válido")

        resultado = decimal_a_sexadecimal(decimal)
        print(f"El equivalente a {decimal} es: {resultado[0]}°, {resultado[1]}', {resultado[2]}''")
    else:
        continuar = True
        while continuar:
            try:
                grados = int(input("Ingrese grados: "))
                continuar = False
            except ValueError:
                print("No es un valor válido")

        continuar = True
        while continuar:
            try:
                minutos = int(input("Ingrese minutos (menor a 60)"))
                if minutos > 59:
                    raise MayorASesenta
                if minutos < 0:
                    raise Negativo
                continuar = False
            except ValueError:
                print("No es un valor válido")
            except MayorASesenta:
                print("Los minutos no pueden ser mayores a 59")
            except Negativo:
                print("Los minutos no pueden ser negativos")

        continuar = True
        while continuar:
            try:
                segundos = int(input("Ingrese segundos (menor a 60)"))
                if segundos > 59:
                    raise MayorASesenta
                if segundos < 0:
                    raise Negativo
                continuar = False
            except ValueError:
                print("No es un valor válido")
            except MayorASesenta:
                print("Los segundos no pueden ser mayores a 59")
            except Negativo:
                print("Los segundos no pueden ser negativos")

        resultado = sexadecimal_a_decimal(grados, minutos, segundos)
        print(f"{grados}°, {minutos}', {segundos}'' = {resultado} en decimal.")

if __name__ == "__main__":
    principal()
