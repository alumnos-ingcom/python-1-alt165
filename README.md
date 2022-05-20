# TP Python #1

## Forma de entrega
* Cada punto debe ser entregado en un archivo independiente
* El nombre de cada archivo debe ser ser `ejercicio` seguido 
del numero de ejercicio mas `.py` (el primer ejercicio sera entonces `ejercicio1.py`
* Cada archivo debe de ser utilizable por otros y funcionar de manera independiente.
* Cada archivo debe seguir la estructura indicada dentro de `plantilla.py`, 
reemplacen con su nombre y nombre de usuario de GitHub. 
* Los archivos del ejercicio deben ir en la carpeta `src` y los tests en `tests`
* En ningún caso se aceptara el uso de variables globales. Toda la información 
necesaria para el funcionamiento de las funciones a desarrollar tienen que ser
pasado como argumentos de las mismas.
* Se provee el prototipo de la funcion a implementar en todos los ejercicios, 
pero pueden crear mas funciones aparte de la pedida.
* Indiquen las pre y poscondiciones de su algoritmo.
* Mantengan separado lo que es entrada, del algoritmo y la salida.
* Siempre que sea posible, los mensajes de commit deben ser descriptivos, nada de
"cambios"

## Importante
Muchas de las funciones pedidas ya se encuentran implementadas como parte de Python, 
implementen las funciones sin depender de esta funcionalidad integrada, sin embargo, 
pueden usar esta funcionalidad para verificar su funcionamiento.
 
Prefieran utilizar lazos indefinidos en lugar de `for`.

## Ejercicios

### 1. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como 
un número decimal, utilice esta formula para calcular los grados centígrados y retorne el 
resultado obtenido. Y viceversa.

``` python
def convertir_a_fahrrenheit(centigrados):
def convertir_a_centigrados(fahrenheit):
```
### 2. Números positivos y negativos

Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero 
utilizando sumas y restas.

``` python
def signo(numero):
```

### 3. Comparación de números

Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:
 * Retornar `-1` si el primero es menor que el segundo
 * Retornar `0` si son iguales
 * Retornar `1` si el primero es mayor que el segundo
 
``` python
def compara(numero, otro_numero):
```

### 4. Suma lenta

Escribir una función que haga la suma entre dos números enteros sin hacer la operación de 
manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones 
resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.

``` python
def suma_lenta(numero, otro_numero):
```

### 5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del 
cociente y resto de dos números enteros.

``` python
def division_lenta(dividendo, divisor):
```

### 6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa

``` python
def ordenar_mayor_a_menor(uno, dos, tres):
def ordenar_menor_a_mayor(uno, dos, tres):
```

### 7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado 
en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido
contrario, devolviendo una `tuple`.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.

``` python
def sexadecimal_a_decimal(horas, minutos, segundos):
def decimal_a_sexadecimal(numero):
```

### 8. Números primos
Escribir una función que indique con `True` si un numero indicado es Primo.

``` python
def es_primo(numero):
```

### 9. Factores Primos
Escribir una función que retorne una `tuple` con factores primos de un numero entero positivo.

``` python
def factores_primos(numero):
```

### 10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo.
Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.

``` python
def es_palindromo(texto):
```

### 11. Multiplos de
Escribir una función que indique con `True` si un número entero es multiplo de otro, utilizando sumas y restas.

``` python
def es_multiplo(numero, multiplo):
```

## Plantilla de entrega individual

```python
################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Reemplazar por el enunciado del ejercicio
"""

# Reemplazar por las funciones a implementar del ejercicio


def principal():
    """
    Descripción del ejercicio
    """
    pass

if __name__ == "__main__":
    principal()
```
