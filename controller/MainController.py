def nuevo_nombre():
    nuevo_nombre=input("Ingrese Nombre: ")
    
    return nuevo_nombre.capitalize()

def nuevo_Color():
    nuevo_Color=input("Ingrese nuevo color: ")
    
    return nuevo_Color

def nueva_Edad():
    nueva_Edad=input("Ingrese edad: ")
    return nueva_Edad

def cambiar_nombre():
    nuevo_nombre = input("Ingrese nuevo nombre:")
    nuevo_nombre.capitalize()
    return nuevo_nombre

def cambiar_color():
    nuevo_color = input("Ingrese nuevo color:")
    return nuevo_color

def modificar_edad():
    nueva_edad = int(input("Ingrese nueva edad:"))
    return nueva_edad

def validar_entrada_int():
    while True:
     opcionM= input("Ingrese una opcion: \n 1. Gatos \n 2. Perros \n 3. Conejos \n 4. Cerrar el programa ")
     try:
        valor=int(opcionM)
        return valor
     except ValueError:
        print("¡La entrada debe ser un numero entero! \n Las opciones validas son del 1 al 4")


def validar_entrada_animales():
    while True:
        opcion=input("1. Listar animales \n 2. Añadir Animales \n 3. Modificar Animal \n 4. Eliminar Animal \n 5. Menu principal ")
        try:
            valor=int(opcion)
            return valor
        except ValueError:
            print("¡La entrada debe ser un numero entero \n Las opciones validas son del 1 al 5")

    
    
    