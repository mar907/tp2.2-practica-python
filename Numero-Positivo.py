while True:
    numero = int(input("Ingresa un número positivo: "))
    if numero > 0:
        break
    else:
        print("El número debe ser positivo. Inténtalo nuevamente.")

print("¡Número válido ingresado:", numero, "!")