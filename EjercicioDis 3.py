x = 0.25
epsilon = 10**(-6)
lado_der = (1 + 2 * x) / (1 + x + x**2)
suma = 0
n = 0

#  Calculamos los términos de la serie
while True:
    n += 1
    # Calculamos el término actual de la serie
    termino = ((-1)**n) * (2 * x**(2 * n) - 2**(n + 1) * x**(4 * n))

    suma += termino
    # Calculamos el lado izquierdo de la ecuación
    lado_izq = suma / (1 - x**(2 * n + 2))
    #
    if abs(lado_izq - lado_der) < epsilon:

        break

# Resultados
print("El número de términos necesarios es:", n)