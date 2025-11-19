from check_sudoku import es_sudoku_valido

def test_valido():
    s = [[1,2,3],[2,3,1],[3,1,2]]
    assert es_sudoku_valido(s)

def test_no_cuadrado():
    s = [[1,2,3],[2,3,1],[3,1]]
    assert not es_sudoku_valido(s)

def test_numero_fuera_rango():
    s = [[1,2,4],[2,3,1],[3,1,2]]
    assert not es_sudoku_valido(s)

def test_fila_repetida():
    s = [[1,1,3],[2,3,1],[3,2,1]]
    assert not es_sudoku_valido(s)

def test_columna_repetida():
    s = [[1,2,3],[1,3,2],[3,1,2]]
    assert not es_sudoku_valido(s)
