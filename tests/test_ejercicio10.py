from src.ejercicio10 import es_palindromo

def test_es_palindromo_mayuscula():
    """prueba con mayusculas"""
    texto = "aSDfgfdsa"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado == True, "No obtenemos un resultado esperado"

def test_es_palindromo_numeros():
    """prueba con mayusculas y numeros"""
    texto = "a1SDfgfds1a"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado == True, "No obtenemos un resultado esperado"
    
def test_no_es_palindromo():
    """prueba con mayusculas"""
    texto = "aSDfgfds"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser un valor lógico"
    assert resultado == False, "No obtenemos un resultado esperado"

if __name__ == "__main__":
    sys.exit(pytest.main())
