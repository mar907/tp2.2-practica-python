numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

print("Números pares:")
for num in range(numero1, numero2 + 1):
    if num % 2 == 0:
        print(num)

print("Números impares:")
for num in range(numero1, numero2 + 1):
    if num % 2 != 0:
        print(num)