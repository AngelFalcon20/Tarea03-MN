
n = int(input("Ingrese el número de elementos en la serie: "))
serie = []
suma = 0

# Ingresamos los valores de la serie
print("Ingrese los valores de la serie:")
for i in range(n):
    valor = float(input("Ingrese el valor de x_" + str(i + 1) + ": "))
    serie.append(valor)

suma = 0

# Calculamos la suma en orden inverso
for i in range(n, 0, -1):

    suma += serie[i - 1]

# Resultado
print("El resultado de la suma es:", suma)