estanteria=[] #es una lista con diccionarios porque es mas facil de editar :(

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\t Presione una tecla para continuar...")

def mostrar():
    if not estanteria:
        print("No tienes libros :[")
        espereTecla()
    else:
        print("\n\t*+--- Libros en la estantería ---+*")
        for i, libro in enumerate(estanteria, start=1):
            print(f"\n\tLibro {i}:")
            for clave, valor in libro.items():
                print(f"\t  {clave}: {valor}")
        espereTecla()

def modificarEstanteria():
    if not estanteria:
        print("No tienes libros :[")
        espereTecla()
    else:
        mostrar()
        num_libro = int(input("\n\tIngresa el número del libro a modificar: "))-1
        try:
            if 0<=num_libro <= len(estanteria):
                libro=estanteria[num_libro]
                for atributo in libro.keys():
                    print(f"¬{atributo}: {libro[atributo]}")
                    resp=input("Desea cambiarlo? ").strip().lower()
                    if resp == "si":
                        nuevo_valor=input("Ingrese el nuevo valor: ").upper()
                        libro[atributo]=nuevo_valor
                print("Se ha realizado con exito :]")
                print(f"{libro}")
                espereTecla()
        except ValueError:
            print("Debes poner un numero >:C")
            espereTecla()

def añadirLibros():
    nuevo_libro={}
    nuevo_libro.update({"nombre":input("ingresa el nombre: ").strip().upper()})
    nuevo_libro.update({"autor":input("ingresa el autor: ").strip().upper()})
    nuevo_libro.update({"genero":input("ingresa el genero: ").strip().upper()})
    nuevo_libro.update({"estado (finalizado/empezado/nada)":input("ingresa el estado: ").strip().upper()})
    nuevo_libro.update({"calificacion (-/5)":input("ingresa la calificacion: ").strip().upper()})
    estanteria.append(nuevo_libro)
    print("\n\t\toperacion realizada con exito!")
    mostrar()

def anadirAtributo():
    nuevo_atr=input("nueva caracteristica a añadir: ").lower().strip()
    valor=input("Valor de la nueva caracteristica: ")
    if not nuevo_atr:
        print("Tiene que poner algo")
        espereTecla()
    else:
        if nuevo_atr in estanteria[0]:
            print("Esta característica ya está...")
            espereTecla()
        else:
            for libro in estanteria:
                libro[nuevo_atr]= valor
            print("Nueva caracteristica añadida!")
            mostrar()

def borrarLibro():
    if not estanteria:
        print("\n\tNo tienes libros :[")
        espereTecla()
    else:
        mostrar()
        num_libro=int(input("\n\tNumero del libro a eliminar: "))-1
        try:
            if 0<=num_libro<len(estanteria):
                eliminado=estanteria.pop(num_libro)
            print(f"\n\tse elimino {eliminado} con exito")
            espereTecla()
        except (ValueError, IndexError):
            print("\n\tDebes poner un numero >:C")
            espereTecla()

def borrarEstanteria():
    input("\n\tEstas segura(o)? ")
    borrarPantalla()
    resp=input("\n\t\tDe verdad? Va a perder todos sus libros...").lower().strip()
    if resp=="si":
        print("borrando...")
        espereTecla()
        estanteria.clear()
        print("La operacion se realizo con exito!")
        espereTecla()
    else:
        print("regresando al menu...")
        espereTecla()

def borrarAtributo():
    if len(estanteria)==0:
        print("No hay caracteristicas a borrar :C")
    else:
        mostrar()
        eliminar=input("Ingresa el nombre de la caracteristica a eliminar: ").lower().strip()
        borrarPantalla()
        if eliminar =="nombre" or eliminar=="autor":
            print("No se puede eliminar ni el nombre ni el autor")
            espereTecla()
        else:
            for libro in estanteria:
                if eliminar in libro:
                    libro.pop(eliminar)
                    print("operacion realizada con exito!")
                    mostrar()
                else:
                    ("No esta ese atributo :C")
    
        



