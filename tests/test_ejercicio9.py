"""Pruebas de la funcion factores_primos del ejercicio9"""
from src.ejercicio9 import factores_primos

def test_negativo():
    """prueba números negativos"""
    numero = -5
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser un valor lógico"
    assert resultado == (0,), "No obtenemos un resultado esperado"

def test_cero():
    """prueba cero"""
    numero = 0
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser un valor lógico"
    assert resultado == (0,), "No obtenemos un resultado esperado"

def test_positivo():
    """prueba números negativos"""
    numero = 300
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser un valor lógico"
    assert resultado == (1, 2, 3, 5), "No obtenemos un resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
