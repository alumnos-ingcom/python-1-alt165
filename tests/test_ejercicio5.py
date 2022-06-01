"""prueba de la funcion división lenta"""
from src.ejercicio5 import division_lenta

def test_dividendo_mayor():
    """prueba dividendo mayor al divisor, resto distinto de cero"""
    dividendo = 5
    divisor = 2
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (2,1), "No obtenemos el resultado esperado"

def test_dividir_iguales():
    """prueba dividendo igual al divisor"""
    dividendo = 5
    divisor = 5
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (1,0), "No obtenemos el resultado esperado"

def test_dividendo_menor():
    """prueba dividendo menor que el divisor"""
    dividendo = 4
    divisor = 5
    resultado = division_lenta(dividendo, divisor)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (0,4), "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
