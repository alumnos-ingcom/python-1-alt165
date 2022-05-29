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
    decimal = ""
    grados = ""
    minutos = ""
    segundos = ""

    print("Para convertir de sexadecimal a decimal precione S")
    print("Para convertir de decimal a sexadecimal presione D")
    while opcion not in ("d", "D", "s", "S"):
        opcion = input()

    if opcion in ("d", "D"):
        while not isinstance(decimal, int):
            decimal = input("Cuál es valor a convertir?: ")
            if decimal.isdecimal():
                decimal = int(decimal)
            else:
                print("No es un valor válido")
            resultado = decimal_a_sexadecimal(decimal)
            print(f"El equivalente a {decimal} es: {resultado[0]}°, {resultado[1]}', {resultado[2]}''")
    else:
        while not isinstance(grados, int):
            grados = input("Ingrese grados: ")
            if grados.lstrip("-").isdecimal():
                grados = int(grados)
            else:
                print("No es un valor válido")

        while not isinstance(minutos, int):
            minutos = input("Ingrese minutos (menor a 60)")
            if minutos.isdecimal():
                minutos = int(minutos)
                if minutos > 60:
                    minutos = ""
                    print("Los minutos deben ser menores a 60")
            else:
                print("No es un valor válido")

        while not isinstance(segundos, int):
            segundos = input("Ingrese segundos (menor a 60)")
            if segundos.isdecimal():
                segundos = int(segundos)
                if segundos > 60:
                    segundos = ""
                    print("Los segundos deben ser menores a 60")
            else:
                print("No es un valor válido")
        resultado = sexadecimal_a_decimal(grados, minutos, segundos)
        print(f"{grados}°, {minutos}', {segundos}'' = {resultado} en decimal.")

if __name__ == "__main__":
    principal()
