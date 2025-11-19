piNumber = 3.14159  # ¿Por qué se usa "PI" aquí?

number = [10, 20, 30, 40, 50]  # ¿Qué representa "g"?

def calc(x, y):
    average = sum(x) / len(x)  # ¿Qué representa "temp"?
    maxValue = max(x)  # ¿Qué representa "z"?
    minValue = min(x)  # ¿Qué representa "w"?
    return average, maxValue, minValue

COLORRED = 1
COLORGREEN = 2
COLORBLUE = 3

# Función con un nombre que no describe su propósito
def statsCalculator():
    # Uso de nombres de variables booleanas poco claros
    isActive = True  # ¿Qué significa "flag"?
    if isActive:
        # Uso de nombres de variables que no describen su propósito
        operationResults = calc(number, piNumber)
        print("Resultados:", operationResults)

for i in range(len(number)):
    print("Elemento", i, ":", number[i])

# Llamada a la función principal
statsCalculator()