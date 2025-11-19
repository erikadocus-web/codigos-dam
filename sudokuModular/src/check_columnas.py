def columnas_sin_repetidos(sudoku):
    numeroDeFilas = len(sudoku)

    indexFilaActual = 0

    for fila in sudoku:
        for numero in fila:
            indexFilaSiguiente = indexFilaActual + 1

            while indexFilaSiguiente < numeroDeFilas:
                try:
                    posicionNumeroFilaSiguiente = sudoku[indexFilaSiguiente].index(
                        numero
                    )

                except ValueError:
                    return False

                else:
                    if posicionNumeroFilaSiguiente == fila.index(numero):
                        return False
                    else:
                        indexFilaSiguiente += 1

        indexFilaActual += 1

    return True


if __name__ == "__main__":

    import sys
    sys.path.append("..")
    
    import casosTest.casos_Test_Sudoku as casosTest

    assert columnas_sin_repetidos(casosTest.irregular_columna) is False
    assert columnas_sin_repetidos(casosTest.numeros_reales) is True

    assert columnas_sin_repetidos(casosTest.correcto) is True
    assert columnas_sin_repetidos(casosTest.irregular_fila) is True
    assert columnas_sin_repetidos(casosTest.numero_repetido_fila_columna) is False
    assert columnas_sin_repetidos(casosTest.numero_repetido_columna) is False
    assert columnas_sin_repetidos(casosTest.numero_no_presente) is False
    assert columnas_sin_repetidos(casosTest.lista_vacia) is True


    print("Todo bien")