from src.ejercicio5 import division_lenta

def test_dividendo_mayor():
    """prueba dividendo mayor al divisor, resto distinto de cero"""
    dividendo = 5
    divisor = 2
    resultado = division_lenta(5, 2)
    assert isinstance(resultado, tuple), "el resultado debe ser una tupla"
    assert resultado == (2,1), "No obtenemos el resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
