import math
a, b, c = 1, 5, 6

def ecuacionSegundoGrado(a,b,c):
    D = b ** 2 - 4 * a * c
    print(D)
    if D < 0:
        print("No se puede")
    else:
        raiz = math.sqrt(D)
        x1 = (-b + D) / 2 * a
        x2 = (-b - D) / 2 * a
        if x1 == x2:
            print("El resultado para ambos casos es " + str(x1))
        else:
            print("Resultado con simbolo mas " + str(x1))
            print("Resultado con simbolo menos " + str(x2))
        

ecuacionSegundoGrado(a,b,c)

