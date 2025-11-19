def loose_change(cents):
    nombreMoneda = ["Quarters", "Dimes", "Nickels", "Pennies"]
    valorMoneda = [25, 10, 5, 1]
    monedasDevueltas = [0, 0, 0, 0]

    if cents <= 0:
        diccionarioCambiado = dict(zip(nombreMoneda, monedasDevueltas))
        return diccionarioCambiado
    else:
        indice = 0
        for moneda in valorMoneda:
            cociente = cents // moneda
            monedasDevueltas[indice] = cociente
            cents = cents % moneda
            indice += 1
        diccionarioCambiado = dict(zip(nombreMoneda, monedasDevueltas))
        return diccionarioCambiado
        

if __name__ == "__main__":
    
    assert loose_change(29) == {"Quarters": 1, "Dimes": 0, "Pennies": 0, "Nickels": 4}

    assert loose_change(-2) == {"Quarters": 0, "Dimes": 0, "Pennies": 0, "Nickels": 0}

    assert loose_change(29) == {"Quarters": 1, "Dimes": 0, "Pennies": 0, "Nickels": 4}

    assert loose_change(5) == {"Quarters": 0, "Dimes": 0, "Pennies": 1, "Nickels": 0} 

    

