numero_palabras = int(input("Ingrese el número de palabras que desea agregar a la lista: "))
lista_palabras = []

for i in range(numero_palabras):
    palabra = input("Ingrese una palabra: ")
    lista_palabras.append(palabra)

print("La lista de palabras es:", lista_palabras)