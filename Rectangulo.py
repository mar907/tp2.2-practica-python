def dibujar_rectangulo(anchura, altura, caracter):
    for i in range(altura):
        for j in range(anchura):
            print(caracter, end='')
        print()

anchura = int(input("Ingrese la anchura del rectángulo: "))
altura = int(input("Ingrese la altura del rectángulo: "))
caracter = input("Ingrese el carácter a utilizar en el dibujo: ")

dibujar_rectangulo(anchura, altura, caracter)