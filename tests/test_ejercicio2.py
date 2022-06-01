"""Prueba de la funcion signo del ejercicio2"""
from src.ejercicio2 import signo

def test_positivo():
    """Probar con valores positivos"""
    numero = 100
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número int"
    assert resultado == 1, "No obtenemos el resultado esperado"

def test_cero():
    """Probar con cero"""
    numero = 0
    resultado = signo(numero)
    assert resultado == 0, "No obtenemos el resultado esperado"

def test_negativo():
    """Probar con valores negativos"""
    numero = -100
    resultado = signo(numero)
    assert resultado == -1, "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
