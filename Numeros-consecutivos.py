numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if numero1 < numero2:
    numeros_consecutivos = list(range(numero1 + 1, numero2))
else:
    numeros_consecutivos = list(range(numero2 + 1, numero1))

print("Números consecutivos:")
for num in numeros_consecutivos:
    print(num)