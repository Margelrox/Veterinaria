from model.Conejo import Conejo
from model.Perro import Perro
from model.Gato import Gato
from model.conexionBDD import *
from controller.MainController import *
from controller.GatoController import *
from controller.ConejoController import *
from controller.PerroController import *
import time

def programaPrincipal():
    while True:
     print(" Menu Principal ")
     opcionM=validar_entrada_int()
    
     if opcionM==4:
      print("Programa finalizado correctamente")
      exit(1)


     if opcionM==1:
      while True:
       print(" Menu Gato")
       opcion=validar_entrada_animales()
       if opcion==5:
         break
       if opcion==1:
         listaGatos()
         time.sleep(2)
         
       if opcion==2:
         nuevoGato= Gato(nuevo_nombre(),nuevo_Color(),nueva_Edad())
         agregarGatos(nuevoGato)
         
       if opcion==3:
         listaGatos()
         time.sleep(2)
         id=int(input("Ingrese la id del gato a modificar "))
         editarGato(id,cambiar_nombre(),cambiar_color(),modificar_edad())
         
       if opcion==4:
         listaGatos()
         time.sleep(2)
         id=int(input("Ingrese la id del gato a eliminar "))
         eliminarGato(id)
         
    #Perros
     if opcionM==2:
      while True:
       print(" Menu Perros")
       opcion= validar_entrada_animales()
       if opcion==5:
         break   
       if opcion==1:
         listaPerros()
         time.sleep(2)
         
      if opcion==2:
         nuevoPerro= Perro(nuevo_nombre(),nuevo_Color(),nueva_Edad())
         agregarPerro(nuevoPerro)
         
      if opcion==3:
         listaPerros()
         time.sleep(2)
         id=int(input("Ingrese la id del perro a modificar "))
         editarPerro(id,cambiar_nombre(),cambiar_color(),modificar_edad())
         
      if opcion==4:
         listaPerros()
         time.sleep(2)
         id=int(input("Ingrese la id del perro a eliminar "))
         eliminarGato(id)
         

    #Conejos
     if opcionM==3:
      while True:
       print(" Menu Conejos")
       opcion= validar_entrada_animales()
       if opcion==5:
         break

       if opcion==1:
         listaConejos()
         time.sleep(2)
         
       if opcion==2:
         nuevoConejo= Conejo(nuevo_nombre(),nuevo_Color(),nueva_Edad())
         agregarGatos(nuevoConejo)
         opcion=0
       if opcion==3:
         listaConejos()
         time.sleep(2)
         id=int(input("Ingrese la id del conejo a modificar "))
         editarConejos(id,cambiar_nombre(),cambiar_color(),modificar_edad())
         
       if opcion==4:
         listaConejos()
         time.sleep(2)
         id=int(input("Ingrese la id del conejo a eliminar "))
         eliminarConejo(id)
         
while True:
  print ("Inicio de sesión")
  print("¿Desea registrar un nuevo usuario?")
  print("1.Si 2.No ")
  opcion=int(input("Esperando opción "))
  if opcion==1:
    correo=input("Ingrese correo: ")
    contrasena=input("Ingrese contraseña: ")
    registrar_usuario(correo,contrasena)
    print("Usuario: "+correo+" Ingresado correctamente")
  elif opcion==2:
   correo = input("Ingrese su correo: ")
   contrasena = input("Ingrese su contraseña: ")

   if autenticar_usuario(correo,contrasena):
    print("Bienvenido")
    programaPrincipal()
    break
   else:
    print("Credenciales incorrectas, intenta nuevamente")