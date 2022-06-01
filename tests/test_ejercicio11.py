"""prueba de la funcion es_multiplo del ejercicio 11
"""
from src.ejercicio11 import es_multiplo

def test_mayor_menor_no_multiplo():
    """prueba primer numero mayor, segundo menor, no es multiplo"""
    numero = 10
    posible_multiplo = 15
    resultado = es_multiplo(numero, posible_multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado is False, "No obtenemos un resultado esperado"

def test_mayor_menor_multiplo():
    """prueba primer numero mayor, segundo menor, si es multiplo"""
    numero = 10
    posible_multiplo = 20
    resultado = es_multiplo(numero, posible_multiplo)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado is True, "No obtenemos un resultado esperado"

def test_iguales_multiplo():
    """prueba numeros iguales"""
    numero = 10
    resultado = es_multiplo(numero, numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado is True, "No obtenemos un resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
