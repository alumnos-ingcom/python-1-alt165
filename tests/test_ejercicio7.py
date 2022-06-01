"""pruebas de funciones sexadecimal_a_decimal, decimal_a_sexadecimal"""
from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_sexadecimal_a_decimal():
    """prueba con numeros iguales"""
    horas = 1
    minutos = 1
    segundos = 1
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(resultado, int), "el resultado debe ser int"
    assert resultado == (3661), "No obtenemos el resultado esperado"

def test_decimal_a_sexadecimal():
    """prueba numero positivos"""
    decimal = 3661
    resultado = decimal_a_sexadecimal(decimal)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (1, 1, 1), "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
