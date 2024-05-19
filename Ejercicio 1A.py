# Primera suma 1/1 + 1/4 + ... + 1/100
suma1 = 0 # Inicializo en cero la suma1
for i in range(1,11):
	valor1 = 1/(i**2)
	suma1 = suma1+valor1

# Segunda suma 1/100 + 1/81 + ... + 1/1
suma2 = 0
for i in range(10, 0, -1):
    valor2 = 1 / (i ** 2)
    suma2 = suma2 + valor2

# Resultados
print(f"Resultado suma1:{suma1:.3}")
print(f"Resultado suma2:{suma2:.3}")

if suma1>suma2:
	print("La primera suma es más precisa.")
elif suma2>suma1:
	print("La segunda suma es más precisa.")
else:
	print("Ambas sumas son precisas.")
