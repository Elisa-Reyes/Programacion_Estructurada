import calificaciones

def main():
    datos = {}
    opcion = True

    while opcion:
        calificaciones.borrarPantalla()
        option=calificaciones.menu_principal()

        match option:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "5":
                calificaciones.borrarPantalla()
                print("\tSe ha terminado la ejecución del sistema\n\n\t\t ::Muchas gracias::")
                calificaciones.esperarTecla()
                opcion=False
            case _:
                calificaciones.borrarPantalla()
                print("\tOpcion invalida, por favor vuelva a intentarlo\n")
                opcion=True



if __name__ == "__main__":
    main()