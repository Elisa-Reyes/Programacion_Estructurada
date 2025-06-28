'''
crear un proyecto que permita administrar or crear peliculas, colocar un menu de opciones: agregar, borrar, modificar, buscar, limpiar una lista de peliculas

notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar listas para almacenar los nombres de las peliculas
'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t ---GESTION DE PELICULAS--- \n\t 1.- agregar \n\t 2.-Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Buscar \n\t 6.- Limpiar \n\t 7.- salir")
    opcion=input("\n\t\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case "7":
            peliculas.borrarPantalla()
            print("\n\t\t Gracias!")
        case _:
            print("\n\t Opcion no valida :(")
            opcion=True
            peliculas.espereTecla()
