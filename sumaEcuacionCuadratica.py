import math
def roots(a,b,c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        x = -b / (2 * a)
        suma = x * 2
        return round(suma, 2)
    else:
        raiz = math.sqrt(d)
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        suma = x1 + x2
        return round(suma, 2)