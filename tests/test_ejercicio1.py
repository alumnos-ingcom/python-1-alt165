"""Prueba de las funciones convertir_a_fahrrenheit, convertir_a_centigrados
del ejercicio1
"""
from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados

def test_fahrenheit():
    """Probar la funcion fahrenheit"""
    numero = 95
    resultado = convertir_a_fahrrenheit(numero)
    assert isinstance(resultado, float), "el resultado debe ser un número float"
    assert resultado == 203, "No obtenemos el resultado esperado"

def test_centigrados():
    """Probar la funcion centrigrados"""
    numero = 203
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "el resultado debe ser un número float"
    assert resultado == 95, "No obtenemos el resultado esperado"
