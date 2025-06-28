import calificaciones

def main():
    datos = []
    opcion = True

    while opcion:
        calificaciones.borrarPantalla()
        calificaciones.menu_principal()

        match opcion:
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
                calificaciones.borrarPantalla()
                print("\tSe ha terminado la ejecución del sistema\n\n\t\t ::Muchas gracias::")
                calificaciones.esperarTecla()
                opc=False
            case _:
                calificaciones.borrarPantalla()
                print("\tOpcion invalida, por favor vuelva a intentarlo\n")
                opc=True



if __name__ == "__main__":
    main()











    