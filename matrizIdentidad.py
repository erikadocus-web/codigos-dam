def matrizIdentidad(matriz):
    n = len(matriz)
    for fila in matriz:
        return len(fila) == n
    

    contadorUnos = 0
    contadorCeros = 0
    for fila in matriz:
        for elemento in fila:
            if elemento == 1:
                posicionUno = fila.index(elemento)
                contadorUnos += 1
            elif elemento != 0:
                contadorCeros += 1

        if contadorUnos != 1 or contadorCeros != 0 or posicionUno != posicionUnoCorrecta:
            return False

        contadorUnos = 0
        posicionUnoCorrecta += 1

    return True

                


if __name__ == "__main__":

    matrix1 = [[1,0,0,0],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]]
    
    assert matrizIdentidad(matrix1)