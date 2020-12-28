
from random import randint, uniform,random
import random
from colorama import init, Fore, Back, Style


print(Fore.GREEN+"        *** EL MULTIDADO ***")
print(Fore.WHITE)
empezar=""

while empezar!="salir":
  empezar=input("Elige que quieres hacer: jugar/salir: ")
  if empezar=="jugar":
    tipo_dado=input("¿qué tipo de dado quieres: numeros,colores ,retos o imitar?: ")
    if tipo_dado=="numeros":
      numero_caras=int(input("¿Cuántas caras quieres que tenga el dado?: "))
      tirar_dado=input("¿Quieres tirar el dado? ")
      while tirar_dado!="no":
          
        if tirar_dado=="si":
          print (Fore.GREEN+str(randint(1,numero_caras)))
          tirar_dado=input(Fore.WHITE+"¿Quieres tirar el dado? ")
        else:
          print ("no reconozco esa respuesta")
          tirar_dado=input("¿Quieres tirar el dado? ")

      continue

            
    elif tipo_dado=="colores":
      lista=[Fore.RED+"rojo",Fore.YELLOW+"amarillo",Fore.GREEN+"verde",Fore.BLUE+"azul"]
      print("los colores son el "+Fore.RED+"rojo, "+Fore.YELLOW+" amarillo, "+Fore.GREEN+"verde y "+Fore.BLUE+" azul"+Fore.WHITE)
      tirar_color=input("¿Quieres tirar el dado: ")
      while tirar_color!="no":

        if tirar_color=="si":
          print(random.choice(lista))
          tirar_color=input(Fore.WHITE+"¿Quieres tirar el dado: ")
        else:
          print ("no reconozco esa respuesta")
          tirar_color=input(Fore.WHITE+"¿Quieres tirar el dado: ")
          
      continue
      
      
    elif tipo_dado=="retos":
      print("ahora ve escribiendo retos. Cuando quieras para ,escribe stop")
      
      lista_retos=[]
      retos=input("dime un reto: ")

      while retos!="stop":
        lista_retos.append(retos)
        retos=input("dime un reto: ")
        
      tirar_retos=input("¿Quieres tirar el dado de los retos? ")
      while tirar_retos!="no":
      
        if tirar_retos=="si":
          print(Fore.GREEN+str(random.choice(lista_retos)))
          tirar_retos=input(Fore.WHITE+"¿Quieres tirar el dado de los retos? ")
        else:
          print ("no reconozco esa respuesta")
          tirar_retos=input("¿Quieres tirar el dado de los retos? ")

    elif tipo_dado=="imitar":
      lista_imitacion=["mono","mejillón","Mariano Rajoi","tigre","tortuga","gallina","elefante","doraemon","elefante","camarero","papa-noel","Rafa Nadal","hormiga","cocinero","oso","rana","cabra","profesor","barrendero"]
      
      imitar_cosas=input("¿quieres tirar el dado? " )
      while imitar_cosas!="no":
        if imitar_cosas=="si":
        
         print(Fore.GREEN+str(random.choice(lista_imitacion)))
         imitar_cosas=input(Fore.WHITE+"¿quieres tirar el dado?" )
        else:
          print ("no reconozco esa respuesta")
          imitar_cosas=input(Fore.WHITE+"¿Quieres tirar el dado: ")

      


print("Se acabo el juego. Muchas gracias por utilizar el Multidado creado por: "+Fore.BLUE+" Javier Fiestas Botella") 