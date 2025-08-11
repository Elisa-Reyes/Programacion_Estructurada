import getpass
from estanterias import estanteria

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla(): 
    input("\n\t\t prima cualquier tecla para continuar ...") 

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
    print("\n\tBienvenido a la Libreria Virtual! \n\t\t1.-  Registro  \n\t\t2.-  Login \n\t\t3.- Salir")
    op=input("\t\t Qué deseas hacer? ").upper().strip() 
    return op
    
#menu menú
def menuM(biblioteca):
    print(f"\n\tBienvenida(o) a tu biblioteca: {biblioteca} \n\t1.- Añadir Libro \n\t2.- Ver Todo \n\t3.- Modificar Libro \n\t4.- Buscar Libro\n\t5.- Borrar Libro \n\t6.- Borrar Todo \n\t7.- Cerrar Sesión")
    #Hay opciones similares, es mejor por numero
    
    

