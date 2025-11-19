def sonNumerosEnteros(sudoku):
    for fila in sudoku:
        for numero in fila:
            if not isinstance(numero, int):
                return False

    return True


def numerosEnRango(sudoku):
    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:
        for numero in fila:
            if numero not in numerosValidos:
                return False

    return True


def checkNumerosValidos(sudoku):
    return sonNumerosEnteros(sudoku) and numerosEnRango(sudoku)



if __name__ == "__main__":

    import sys
    sys.path.append("..")

    import casosTest.casos_Test_Sudoku as casosTest

    assert sonNumerosEnteros(casosTest.correcto) is True
    assert sonNumerosEnteros(casosTest.numero_repetido_fila_columna) is True
    assert sonNumerosEnteros(casosTest.numero_repetido_columna) is True
    assert sonNumerosEnteros(casosTest.numero_no_presente) is True
    assert sonNumerosEnteros(casosTest.numero_fuera_del_rango) is True
    assert sonNumerosEnteros(casosTest.caracteres) is False
    assert sonNumerosEnteros(casosTest.numeros_reales) is False
    assert sonNumerosEnteros(casosTest.irregular_fila) is True
    assert sonNumerosEnteros(casosTest.irregular_columna) is True
    assert sonNumerosEnteros(casosTest.lista_vacia) is True
    
    print("Casos test pasados")