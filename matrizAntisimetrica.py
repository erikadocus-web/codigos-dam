def matrizAntisimetrica(matriz):

    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != -matriz[j][i]:
                return False
            
    for fila in matriz:
        return len(matriz) == len(fila)
        

    

if __name__ == '__main__':
    matriz2 = ([[0, 1, 2],[-1, 0, 3],[-2, -3, 0]])

    assert matrizAntisimetrica(matriz2)

    matriz1 = ([[0, 0, 0],[0, 0, 0],[0, 0, 0]])
    
    assert matrizAntisimetrica(matriz1)

    matriz4 = [[1,0,0,0],
               [0,1,1,0],
               [0,0,0,1]]
    
    assert not matrizAntisimetrica(matriz4)

    matriz5 = [[1,0,0,0,0,0,0,0,0]]

    assert not matrizAntisimetrica(matriz5)