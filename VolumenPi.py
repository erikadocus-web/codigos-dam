import math

def volumen():
    entradaNumero = input("Inserta la cantidad de caracteres del numero PI dependiendo del volumen deseado ")
    entradaNumero = list(entradaNumero)
    
    pi_str = f"{math.pi:.100f}"
    pi_list = list(pi_str[:100])
    del pi_list[1]
    
    volumen = 0
    
    for num in range(len(entradaNumero)):
        if entradaNumero[num] == pi_list[num]:
            volumen = volumen + 1
            
    print(f"Volumen seleccionado: {volumen}")
            

volumen()