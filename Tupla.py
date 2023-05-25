meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

numero = int(input("Ingresa un número entre 1 y {}: ".format(len(meses))))

if 1 <= numero <= len(meses):
    mes = meses[numero - 1]
    print("El mes correspondiente al número {} es {}.".format(numero, mes))
else:
    print("Error: El número ingresado está fuera del rango válido.")
    
""" El método format() es un método integrado de las cadenas de texto en Python que se utiliza 
para formatear cadenas. Permite crear cadenas de salida más complejas combinando valores 
variables con un texto estático en una cadena formateada.
El método format() toma uno o más argumentos y los inserta en una cadena en los lugares 
designados por marcadores de posición. Estos marcadores de posición se representan con llaves
{} dentro de la cadena y actúan como espacios reservados para los valores que se deben 
insertar.
El método format() puede realizar las siguientes acciones:
Sustitución de valores: Puedes proporcionar valores para reemplazar los marcadores de posición
en la cadena formateada. Los valores pueden ser variables, constantes u objetos.
Especificación de formato: Puedes utilizar especificaciones de formato dentro de los 
marcadores de posición para controlar la forma en que se muestran los valores. Por ejemplo, 
puedes especificar el número de decimales en un número o el ancho de un campo. """