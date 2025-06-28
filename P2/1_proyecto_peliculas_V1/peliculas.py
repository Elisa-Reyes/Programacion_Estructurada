peliculas=[]

#limpiar es para borrar todo de la lista, preguntar primero y verificar de que haya algo en la lista
#Mostrar es para mostrar peliculas una por una, enumeradas que empiece en el 1

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\t Presione una tecla para continuar...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t Agregar Peliculas \n")
    peliculas.append(input("Ingrese el nombre: ").upper().strip())
    print("\n\t\t LA OPERACION SE REALIZO CON EXITO!")

def mostrarPeliculas():
    borrarPantalla()
    for i, pelicula in enumerate(peliculas, start=1):
        print(i, pelicula)

def borrarPeliculas():
    borrarPantalla()
    print("vas a borrar TODAS las peliculas")
    resp=input("\n\t estas seguro de que deseas borrar todas las peliculas?").lower()
    if resp=="si":
        peliculas.clear()
        print("\n\t\t LA OPERACION SE REALIZO CON EXITO!")

def buscarPeliculas():
    borrarPantalla()
    buscar=input("nombre: ").upper().strip()
    if not(buscar in peliculas):
        print("no existe")
    else:
        for i in range(0,len(peliculas)):
            print(f"la pelicula {buscar} esta en: {i+1}")
            encontro+=1
        print(f"tenemos {encontro} pelicula(s) con ese titulo")
        print("\n\t\t LA OPERACION SE REALIZO CON EXITO!")

def modificarPeliculas():
    borrarPantalla()
    buscar=input("nombre: ").upper().strip()
    encontro=0
    if not(buscar in peliculas):
        print("la pelicula no esta")
    else:
        for i in range(0,len(peliculas)):
            if buscar==peliculas[i]:
                resp=input("deseas actualizar la pelicula?").lower
                if resp=="si":
                    peliculas[i]=input("introduce el nuevo nombre de la pelicula: ").upper().strip()
                    encontro+=1
                    print("\n\t\t LA OPERACION SE REALIZO CON EXITO!")
        print(f"se modifico {encontro} pelicula(s) con este titulo")       

def limpiarPeliculas():
    borrarPantalla()
    buscar=input("nombre: ").upper().strip()
    encontro=0
    if not(buscar in peliculas):
        print("la pelicula no esta")
    else:
        resp="si"
        for i in range(0,len(peliculas)):
            if buscar==peliculas[i]:
                resp=input("deseas eliminar la pelicula?").lower()
                if resp=="si":
                    peliculas.remove(peliculas[i])
                    encontro+=1
                    print("\n\t\t LA OPERACION SE REALIZO CON EXITO!")

                
            