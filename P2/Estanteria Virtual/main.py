import libreria

opcion=True

while opcion:
    libreria.borrarPantalla()
    print("\n\t\t Bienvenida(o) a la estantería digital \n\t\t ------------------------------------- \n\t1.- Mostrar libros \n\t2.- Modificar estanteria \n\t3.- Añadir libro \n\t4.- Añadir caracteristica \n\t5.- Borrar libro \n\t6.- Borrar estanteria \n\t7.- Borrar caracteristica \n\t8.- Salir")
    option=input("\n\tQué desea hacer? ").lower().strip()
   
    match option:
        case "1":
            libreria.borrarPantalla()
            libreria.mostrar()
        case "2":
            libreria.borrarPantalla()
            libreria.modificarEstanteria()
        case "3":
            libreria.borrarPantalla()
            libreria.añadirLibros()
        case "4":
            libreria.borrarPantalla()
            libreria.anadirAtributo()
        case "5":
            libreria.borrarPantalla()
            libreria.borrarLibro()
        case "6":
            libreria.borrarPantalla()
            libreria.borrarEstanteria()
        case "7":
            libreria.borrarPantalla()
            libreria.borrarAtributo()
        case "8":
            libreria.borrarPantalla()
            print("Hasta pronto :D")
            opcion=False  
        case _:
            print("\n\t Opcion no valida :(")
            opcion=True
            libreria.espereTecla()


