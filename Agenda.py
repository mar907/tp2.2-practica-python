agenda = {}

while True:
    nombre = input("Ingresa el nombre del contacto (o 'no' para terminar): ")
    
    if nombre.lower() == 'no':
        break
    
    if nombre in agenda:
        print("El nombre ya existe en la agenda. Por favor, ingresa un nombre diferente.")
        continue
    
    telefono = input("Ingresa el número de teléfono: ")
    agenda[nombre] = telefono

print("\nAgenda de contactos:")
for nombre, telefono in agenda.items():
    print("Nombre: {}, Teléfono: {}".format(nombre, telefono))
    
""" El método lower() es un método integrado en Python que se utiliza en las cadenas de texto 
para convertir todos los caracteres en minúsculas.
Cuando se aplica el método lower() a una cadena, se crea y retorna una nueva cadena con todos
los caracteres en minúsculas. Si la cadena original ya está en minúsculas, el método lower() 
no tiene ningún efecto y simplemente se devuelve la misma cadena sin cambios. """