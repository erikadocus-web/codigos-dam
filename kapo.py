import random

def crearBaraja():
    palos = ["copas", "oros", "espadas", "bastos"]
    numeradas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    baraja = [f"{numero} de {palo}" for palo in palos for numero in numeradas]
    return baraja

def jugadores():
    numJugadores = input("Ingrese numero de jugadores ")
    numJugadores = int(numJugadores)
    return numJugadores

def repartirCartas(baraja, numJugadores):
    random.shuffle(baraja)

baraja = crearBaraja()
numJugadores = jugadores()

repartirCartas()
    

    


#def repartirCartas():
#    PosicionPrimeraCarta = random.randint(1, 12)
#    PosicionSegundaCarta = random.randint(1, 12)
#    PosicionTerceraCarta = random.randint(1, 12)
#    PosicionCuartaCarta = random.randint(1, 12)
#    manoActual[0] = PosicionPrimeraCarta
#    manoActual[1] = PosicionSegundaCarta
#    manoActual[2] = PosicionTerceraCarta
#    manoActual[3] = PosicionCuartaCarta
#    print(manoActual)
#
#    numeroSeleccionado1 = input("Seleccione un numero del 1 al 4: ")
#    numeroSeleccionado1 = int(numeroSeleccionado1) - 1
#    while numeroSeleccionado1 > 4:
#        numeroSeleccionado1 = input("Seleccione otro numero del 1 al 4: ")
#        numeroSeleccionado1 = int(numeroSeleccionado1)
#        
#    numeroSeleccionado2 = input("Seleccione otro numero del 1 al 4: ")
#    numeroSeleccionado2 = int(numeroSeleccionado2) - 1
#    while numeroSeleccionado2 > 4 or numeroSeleccionado1 == numeroSeleccionado2:
#        numeroSeleccionado2 = input("Seleccione otro numero del 1 al 4: ")
#        numeroSeleccionado2 = int(numeroSeleccionado2)
#
#    visualizacionCartaUno = manoActual[numeroSeleccionado1]
#    visualizacionCartaDos = manoActual[numeroSeleccionado2]
#    print(f"Mano cartas visibles: {visualizacionCartaUno}, {visualizacionCartaDos}")

#def ronda():
#    cartasRecogida = []
#    cartasDejadas = []
    
    
    
#repartirCartas()