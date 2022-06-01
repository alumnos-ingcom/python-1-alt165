"""Prueba de la función suma_lenta del ejercicio4"""
from src.ejercicio4 import suma_lenta

def test_positivo():
    """Prueba con numeros positivos
    """
    numero1 = 100
    numero2 = 200    
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número int"
    assert resultado == numero1 + numero2, "No obtenemos el resultado esperado"

def test_cero():
    """Prueba con un numero igual a 0, la comparacion es contra el primer
    argumento
    """
    numero1 = 0
    numero2 = 10
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número int"
    assert resultado == numero2, "No obtenemos el resultado esperado"

def test_negativo():
    """Prueba con numeros negativos
    """
    numero1 = -100
    numero2 = -200    
    resultado = suma_lenta(numero1, numero2)
    assert isinstance(resultado, int), "el resultado debe ser un número int"
    assert resultado == numero1 + numero2, "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
