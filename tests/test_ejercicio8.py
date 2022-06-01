"""Pruebas de la funcion es primo del ejercicio8"""
from src.ejercicio8 import es_primo

def test_negativo():
    """prueba números negativos"""
    numero = -5
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado is False, "No obtenemos un resultado esperado"

def test_si_es_primo():
    """prueba número primo"""
    numero = 5
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado is True, "No obtenemos un resultado esperado"

def test_no_es_primo():
    """prueba número primo"""
    numero = 6
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado is False, "No obtenemos un resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
