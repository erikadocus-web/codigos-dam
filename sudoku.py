#checkcuadrado
#checknumerosvalidos
#checkfilas checkcolumnas

def checkCuadrado(sudoku):
    fila = 0
    longitudColumna = len(sudoku)
    while fila < longitudColumna:
        longitudFila = len(sudoku[fila])

        if longitudFila == longitudColumna:
            fila += 1
        else:
            return False
        
    return True

def checkNumerosValidos(sudoku):
    for fila in sudoku:
        for numero in fila:
            if numero not in range(1, len(sudoku)+1):
                return False
    return True


def checkFilas(sudoku):
    for lista in sudoku:
        numerosContados = {}
        for number in lista:
            if number not in numerosContados:
                numerosContados[number] = 1
            else:
                numerosContados[number] += 1
            
            if numerosContados[number] > 1:
                return False
    return True

def checkColumnas(sudoku):
    


#Cambiar nombre de los casos tests

if __name__ == "__main__":

    sudoku0 = [[1, 2, 3],
               [2, 3, 1],
               [3, 1, 2]]
    
    assert checkCuadrado(sudoku0), "Es Cuadrado"
    assert checkNumerosValidos(sudoku0), "Numeros Validos"


    sudoku1 = [[1, 2, 3, 4],
              [2, 3, 1, 3],
              [3, 1, 2, 3],
              [4, 4, 4, 2]]
    assert checkCuadrado(sudoku1), "Es Cuadrado"
    assert checkNumerosValidos(sudoku1), "Numeros Validos"


    sudoku2 =   [[1, 2, 3],
                [2, 3, 1],
                [2, 3, 1]]
    assert checkCuadrado(sudoku2), "Es Cuadrado"
    assert checkNumerosValidos(sudoku2), "Numeros Validos"

    sudoku3 =    [[1, 2, 3, 4],
                 [2, 3, 1, 2],
                 [4, 1, 2, 3],
                 [2, 3, 1, 4]]
    assert checkCuadrado(sudoku3), "Es Cuadrado"
    assert checkNumerosValidos(sudoku3), "Numeros Validos"

    sudoku4 =    [[1, 2, 3, 4, 5],
                 [2, 3, 1, 5, 6],
                 [4, 5, 2, 1, 3],
                 [3, 4, 5, 2, 1],
                 [5, 6, 4, 3, 2]]
    assert checkCuadrado(sudoku4), "Es Cuadrado"
    assert not checkNumerosValidos(sudoku4), "Numeros no Validos"

    sudoku5 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]
    assert checkCuadrado(sudoku5), "Es Cuadrado"
    assert not checkNumerosValidos(sudoku5), "Numeros no Validos"

    sudoku6 =    [[1, 1.5],
                 [1.5, 1]]
    assert checkCuadrado(sudoku6), "Es Cuadrado"
    assert not checkNumerosValidos(sudoku6), "Numeros no Validos"

    sudoku7 =    [[1, 2, 3],
                  [2, 3, 1]]
    assert not checkCuadrado(sudoku7), "No es Cuadrado"
    assert checkNumerosValidos(sudoku7), "Numeros Validos"

    sudoku8 = [[1, 2, 3],[2, 3, 1],[3, 1]]
    assert not checkCuadrado(sudoku8), "No es Cuadrado"
    assert checkNumerosValidos(sudoku8), "Numeros Validos"

    sudoku9 = [[]]
    assert not checkCuadrado(sudoku9), "Es Cuadrado"
    assert not checkNumerosValidos(sudoku9), "Numeros no Validos"

