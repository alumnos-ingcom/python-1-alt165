#import sys
#import pytest
#from ejercicio2 import signo
from src.ejercicio2 import signo

def test_positivo():
    numero = 100
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número int"
    assert resultado == 1, "No obtenemos el resultado esperado"

def test_cero():
    numero = 0
    resultado = signo(numero)
    assert resultado == 0, "No obtenemos el resultado esperado"
    
def test_negativo():
    numero = -100
    resultado = signo(numero)
    assert resultado == -1, "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
