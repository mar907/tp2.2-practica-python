while True:
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))

    if numero2 > numero1:
        break
    else:
        print("El segundo número debe ser mayor que el primero. Inténtalo nuevamente.")

print("Primer número:", numero1)
print("Segundo número:", numero2)