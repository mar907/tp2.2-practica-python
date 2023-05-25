numero = int(input("Ingresa un número: "))

tabla_multiplicar = []
for i in range(1, 11):
    resultado = numero * i
    tabla_multiplicar.append(resultado)

print(tabla_multiplicar)