def filas_sin_repetidos(sudoku):
    """Devuelve True si en cada fila no hay valores repetidos."""
    for fila in sudoku:
        seen = set()
        for x in fila:
            if x in seen:
                return False
            seen.add(x)
    return True

if __name__ == "__main__":

    import sys
    sys.path.append("..")

    import casosTest.casos_Test_Sudoku as casosTest

    assert filas_sin_repetidos(casosTest.correcto) is True
    assert filas_sin_repetidos(casosTest.numero_repetido_fila_columna) is False
    assert filas_sin_repetidos(casosTest.numero_repetido_columna) is True
    assert filas_sin_repetidos(casosTest.numero_no_presente) is False
    assert filas_sin_repetidos(casosTest.numero_fuera_del_rango) is True
    assert filas_sin_repetidos(casosTest.caracteres) is True
    assert filas_sin_repetidos(casosTest.numeros_reales) is True
    assert filas_sin_repetidos(casosTest.irregular_fila) is True
    assert filas_sin_repetidos(casosTest.irregular_columna) is True
    assert filas_sin_repetidos(casosTest.lista_vacia) is True
    
    print("Casos test pasados")

