""" pruebas de funciones ordenar_mayor_a_menor, ordenar_menor_a_mayor del ejercicio6"""
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

def test_mayor_menor_iguales():
    """prueba con numeros iguales"""
    numero1 = 5
    numero2 = 5
    numero3 = 5
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (5, 5, 5), "No obtenemos el resultado esperado"

def test_menor_mayor_iguales():
    """prueba con numeros iguales"""
    numero1 = 5
    numero2 = 5
    numero3 = 5
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (5, 5, 5), "No obtenemos el resultado esperado"

def test_mayor_menor_negativos():
    """Prueba con numeros negativos"""
    numero1 = -5
    numero2 = -4
    numero3 = -3
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (-3, -4, -5), "No obtenemos el resultado esperado"

def test_menor_mayor_negativos():
    """Prueba con numeros negativos"""
    numero1 = -1
    numero2 = -4
    numero3 = -3
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (-4, -3, -1), "No obtenemos el resultado esperado"

def test_mayor_menor_positivos():
    """Prueba con numeros positivos"""
    numero1 = 5
    numero2 = 0
    numero3 = 3
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (5, 3, 0), "No obtenemos el resultado esperado"

def test_menor_mayor_positivos():
    """Prueba con numeros positivos"""
    numero1 = 45
    numero2 = 54
    numero3 = 44
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (44, 45, 54), "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
