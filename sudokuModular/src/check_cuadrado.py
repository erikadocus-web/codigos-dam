def es_cuadrado(sudoku):
    """Devuelve True si sudoku es una matriz N x N (todas las filas tienen longitud N)."""
    if not isinstance(sudoku, list) or len(sudoku) == 0:
        return False
    n = len(sudoku)
    for fila in sudoku:
        if not isinstance(fila, list) or len(fila) != n:
            return False
    return True


if __name__ == "__main__":
    
    import sys
    sys.path.append("..")
    
    import casosTest.casos_Test_Sudoku as casosTest

    assert es_cuadrado(casosTest.irregular_columna) is False
    assert es_cuadrado(casosTest.irregular_fila) is False
    assert es_cuadrado(casosTest.numeros_reales) is True

    assert es_cuadrado(casosTest.correcto) is True
    assert es_cuadrado(casosTest.numero_repetido_fila_columna) is True
    assert es_cuadrado(casosTest.numero_repetido_columna) is True
    assert es_cuadrado(casosTest.numero_no_presente) is True
    assert es_cuadrado(casosTest.lista_vacia) is False

    print("Todo bien")
    
