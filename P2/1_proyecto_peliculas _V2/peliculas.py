#peliculas={
 #   "nombre":"",
  #  "categoria":"",
   # "clasificacion":"",
    #"genero":"",
    #"idioma":""
#}

#crear un diccionario que permita almacenar todos los atributos
pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\t Presione una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("\n\t\t Agregar peliculas")
    pelicula.update({"nombre":input("ingresa el nombre: ").strip().upper()})
    pelicula.update({"categoria":input("ingresa la categoria: ").strip().upper()})
    pelicula.update({"clasificacion":input("ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("ingresa el genero: ").upper().strip()})
    print("\n\t\t La operacion fue realizada con exito: ")

def mostrarPeliculas():
    borrarPantalla()
    print("Mostrar peliculas")
    if len(pelicula)>0:
        for i, peliculas in enumerate(pelicula, start=1):
            print(i, pelicula)
    else:
        print("No hay peliculas")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t Estas seguro?")
    resp=input("si/no").lower()
    if resp=="si":
        if len(pelicula)>0:
            pelicula.clear()
            print("\n\t la accion se realizo con exito")
        else:
            print("No hay peliculas")
 

def agregarPeliculas():
    print("\n\t agregar caracteristicas ")
    atributo=input("nomre de la caracteristica: ").lower().strip()
    valor_atributo=input("valor de la caracteristica").upper().strip()
    pelicula.update({atributo:valor_atributo})

#modificar tiene que mostrar la primera caracteristica del diccionario, 
#luego preguntar y asi uno por uno si se quiere modificar el valor del atributo
def modificarPeliculas():
    borrarPantalla()
    if len(pelicula)==0:
        print("no hay atributos a editar")
    else:
        for atributo, valor_atributo in pelicula.items():
            print({atributo:valor_atributo})
            resp=input("desea cambiar un atributo? (si/no): ").lower().strip()

            if resp=="si":
                nuevo_valor=input(f"escribe el nuevo valor para {atributo}: ")
                pelicula[atributo]=nuevo_valor
        print("tu atributo se ha actualizado!")
        print(pelicula)

def borrarCarPeliculas():
    borrarPantalla()
    if len(pelicula)==0:
        print("no hay atributos a borrar")
    else:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
        
        resp=input("deseas borrar alguna caracteristica? si/no: ").lower().strip()

        if resp=="si":
            i=input("ingresa la caracteristica que deseas eliminar: ").lower().strip()
            if not(i in pelicula):
                print("no se encontro la caracteristica")
            else:
                for i in pelicula:                    
                    del({i})
                    print("se elimino")

