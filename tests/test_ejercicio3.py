"""Prubas de funcion compara y absoluto del ejercicio 3
"""
from src.ejercicio3 import absoluto, compara

def test_positivo_absoluto():
    """prueba con valor positivo
    """
    numero = 100
    resultado = absoluto(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número int"
    assert resultado == numero, "No obtenemos el resultado esperado"

def test_negativo_absoluto():
    """prueba con valor negativo
    """
    numero = -100
    resultado = absoluto(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número int"
    assert resultado == numero * (-1), "No obtenemos el resultado esperado"
    
def test_menor_mayor():
    """Primer número menor que el segundo"""
    numero1 = -5
    numero2 = 5
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "el resultado debe ser una tupla"
    assert resultado == -1, "No obtenemos el resultado esperado"

def test_mayor_menor():
    """primer número mayor que el segundo"""
    numero1 = 10
    numero2 = 5
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "el resultado debe ser una tupla"
    assert resultado == 1, "No obtenemos el resultado esperado"

def test_iguales():
    """Ambos números iguales"""
    numero1 = 10
    numero2 = 10
    resultado = compara(numero1, numero2)
    assert isinstance(resultado, int), "el resultado debe ser una tupla"
    assert resultado == 0, "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
