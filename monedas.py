def cambio_monedas(eurosIngresados):
    listaMonedas = [5, 2, 1]
    cantidadMonedas = []

    for moneda in listaMonedas:
        cantidad = eurosIngresados // moneda
        eurosIngresados %= moneda
        cantidadMonedas.append(cantidad)

    print(cantidadMonedas)

cambio_monedas(2)