
def greatest(lista):
    if len(lista) == 0:
        print(0)
    else:
        listaOrdenada = sorted(lista, reverse=True)
        print(listaOrdenada[0])

greatest([5, 8 ,8 ,6])