'''
crear un proyecto que permita administrar or crear peliculas, colocar un menu de opciones: agregar, borrar, modificar, buscar, limpiar una lista de peliculas

notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.-utilizqar diccionarios para almacenar los tributos (nombre, categoria,clasificacion,genero,idioma)
'''

import peliculas

opcion=True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t ---GESTION DE PELICULAS--- \n\t 1.- crear \n\t 2.-Borrar \n\t 3.- Mostrar \n\t 4.- Agregar caracteristicas \n\t 5.- Modificar caracteristicas \n\t 6.- Borrar caracteristicas \n\t 7.- salir")
    opcion=input("\n\t\t Elige una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.borrarCarPeliculas()
            peliculas.espereTecla()
        case "7":
            peliculas.borrarPantalla()
            print("\n\t\t Gracias!")
        case _:
            print("\n\t Opcion no valida :(")
            opcion=True
            peliculas.espereTecla()

