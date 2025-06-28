#lista = [
 #   ("Ruben", 10, 10, 10,
  #  "Andres", 0.0, 9.5, 6.8)
#]


def borrarPantalla():
    import os
    os.system("clear")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
    print("`n\ \U0001F4DD` .::Sistema de Gestion de Calificaciones::.`\U0001F4DD` \n\t '`\u2705` Agregar \n\t `\u2705` Mostrar \n\t `\u2705` Calcular promedios \n\t `\u2705` Buscar \n\t `\u2705`Salir")
    opcion = input("Elige una opcion (1-4): ")
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("Agregar Calificaciones: ")
    nombre = input("Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1,4):
       continua = True 

       while continua:
        try:
         #calificaciones.append (float(input(f"Calificacion #{i}")))
         cal=float(input(f"Calificacion #{i}"))
         if cal>=0 and cal<=10:
            calificaciones.append(cal)
            continua=False
         else:
            print("Ingresa un valor comprendido entre el 0 y el 10")
        except ValueError:
          print("Ingresa un valor numerico")

    lista.append([nombre] + calificaciones)
    print("Accion realizada con exito")

def mostrar_calificaciones(lista):
   borrarPantalla()
   print("Mostrar las Calificaciones")
   if len(lista)>0:
      print(f"{'Nombre':<15} {'Calif.1':<10} {'Calif.2':<10} {'Calif.3':<10}")
      print("-" * 50)
      for fila in lista:
         print(f"{fila [0]}   {fila[1]}    {fila[2]}     {fila[3]}")
      print("-" * 50)
      cuantos=len(lista)
      print(f"Son {cuantos} alumnos")
   else:
      print ("No hay calificaciones en el sistma")

def calcular_promedios(lista):
   borrarPantalla()
   print("Promedios de los Alumnos")
   if len(lista)>0:
      print(f"{'Nombre':<15} {'Promedio':<10}")
      print("-" * 40)
      promedio_grupal = 0
      for fila in lista:
         nombre = fila[0]
         #promedio = (fila[1]+fila[2]+fila[3])/3
         promedio=sum(fila[1:])/3
         print(f"{nombre:<15}{promedio:.2f}")
         promedio_grupal+=promedio
         
      print("-" * 40)
      promedio_grupal=promedio_grupal/len(lista)
      print(f"El promedio del grupo es : {promedio_grupal:.2f}")
      
      cuantos=len(lista)
      print(f"Son {cuantos} alumnos")
   else:
      print ("n\t\ \u274C No hay calificaciones en el sistma `\u274C`  ")