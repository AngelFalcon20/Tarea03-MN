# Suma 1
suma1 = 0 # Inicializo en cero la suma1
for i in range(1,11):
	valor1 = 1/(i**3)
	suma1 = suma1+valor1

# Suma 2
suma2 = 0 # Inicializo en cero la suma2
for i in range(10, 0, -1):
    valor2 = 1 /(i**3)
    suma2 = suma2+valor2

# Resultados
print(f"Resultado suma1:{suma1:.4}")
print(f"Resultado suma2:{suma2:.4}")

if suma1>suma2:
	print("La primera suma es más precisa.")
elif suma2>suma1:
	print("La segunda suma es más precisa.")
else:
	print("Ambas sumas son precisas.")




