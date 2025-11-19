from src.check_cuadrado import es_cuadrado
from src.check_numeros import checkNumerosValidos
from src.check_filas import filas_sin_repetidos
from src.check_columnas import columnas_sin_repetidos

def es_sudoku_valido(sudoku):

    if not es_cuadrado(sudoku):
        return False
    if not checkNumerosValidos(sudoku):
        return False
    if not filas_sin_repetidos(sudoku):
        return False
    if not columnas_sin_repetidos(sudoku):
        return False
    return True

if __name__ == "__main__":
    
    import sys
    sys.path.append("..")
    
    import casosTest.casos_Test_Sudoku as casosTest

    assert es_sudoku_valido(casosTest.correcto) is True
    assert es_sudoku_valido(casosTest.numero_repetido_fila_columna) is False
    assert es_sudoku_valido(casosTest.numero_repetido_columna) is False
    assert es_sudoku_valido(casosTest.numero_no_presente) is False
    assert es_sudoku_valido(casosTest.numero_fuera_del_rango) is False
    assert es_sudoku_valido(casosTest.caracteres) is False
    assert es_sudoku_valido(casosTest.numeros_reales) is False
    assert es_sudoku_valido(casosTest.irregular_fila) is False
    assert es_sudoku_valido(casosTest.irregular_columna) is False
    assert es_sudoku_valido(casosTest.lista_vacia) is False
    
    print("Casos test pasados")
