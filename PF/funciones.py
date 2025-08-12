import openpyxl
from conexionBD import *
import funciones
import os

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla(): 
    input("\n\t\t Oprima cualquier tecla para continuar ...") 

def arte():
    gato='''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⣾⡄⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣆⢀⣿⣿⣦⣴⣤⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣼⣿⣿⡟⢻⡟⢻⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠋⠀⢻⣿⣿⡛⠛⠁⠈⠻⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀⠘⢿⣿⣶⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠀⠀⠀⠹⠿⠟⠋⠀⠀⠀⠀⠀⠘⠛⠟⠃⠀⠀
'''
    print(f"\n\t{gato}")

def salir():
    print("\n\t\033[38;2;255;105;180m Hasta luego!\033[0m")
    idk= '''
        ⠀⠀⠀⠀⣠⠤⣄⣀⣠⠤⣄⠀⠀⠀
        ⠀⠀⠀⡼⢡⠖⢦⠉⡴⠲⡌⢧⠀⠀
        ⠀⡴⢋⣁⡘⢦⠾⠀⠷⡴⢃⣈⡙⢦
        ⠰⡇⢯⠀⡷⠀⢠⠤⣄⠀⢾⠀⡽⢸
        ⠀⠹⢬⠉⢁⡴⠋⠀⠘⢦⡈⠉⡥⠏
        ⠀⠀⠘⣆⠘⢧⣤⠤⣤⡼⠃⣰⠃⠀
        ⠀⠀⠀⠈⠳⢤⣀⣀⣀⡤⠖⠁
    '''
    print(f"\n\t{idk}")

#menu usuarios
def menuU():
    print("\n\t𖹭.- Bienvenido a la Libreria Virtual! \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir")
    op=input("\t\t ¿Qué deseas hacer? ").upper().strip() 
    return op
    
#menu menú
def menuM(biblioteca):
    print(f"\n\t𖹭.- Bienvenida(o) a tu biblioteca: {biblioteca} \n\t1.- Añadir Libro \n\t2.- Ver Todo \n\t3.- Modificar Libro \n\t4.- Buscar Libro\n\t5.- Borrar Libro \n\t6.- Borrar Todo \n\t7.- Exportar a Excel \n\t8.- Cerrar Sesión")
    #Hay opciones similares, es mejor por numero
    
def exportar(usuario_id,biblioteca):
    print("\n\t\tExportar a Excel! 𖹭")
    si=input("🍒.- ¿Quieres a exportar ahora (si/no)? ").lower().strip()
    if si=="si":
        try:
            cursor.execute("SELECT id, titulo, autor, clasificacion, genero, estanteria FROM libros WHERE usuario_id = %s", (usuario_id,))
            archivo_excel=openpyxl.Workbook()
            archivo_excel.active.append(["ID", "Título", "Autor", "Clasificación", "Género", "Estantería"])
            for libro in cursor.fetchall():
                archivo_excel.active.append(libro)
            nombre=(f"biblioteca_{biblioteca}.xlsx")
            archivo_excel.save(f"biblioteca_{biblioteca}.xlsx")
            ruta=os.path.abspath(nombre)
            print(f"Documento exportado correctamente: {ruta}! *🫧")
            return True
        except Exception as e:
            print(f"Ocurrió un problema al exportar: {e} :C")
            funciones.arte()
            return False   

