import funciones
from estanterias import estanteria
from usuarios import usuarios
import getpass

#inicia sesion -> menu. todo va en funciones, aqui mantener simple para hacerlo limpio, seguro y bajo mis condiciones

def main():
    op=True
    while op:
        op=funciones.menuU()
        if op=="1" or op=="REGISTRO":
            funciones.borrarPantalla()
            usuarios.registrar()
        elif op=="2" or op=="LOGIN":
            funciones.borrarPantalla()
            print("\n\t\t°.- Inicio de sesion 𖹭")     
            email=input("\t ⊹Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t ⊹Ingresa tu contraseña: ").strip() 
            lista_usuarios=usuarios.login(email,password)

            if lista_usuarios:
                funciones.borrarPantalla()
                main_menu(lista_usuarios[0],lista_usuarios[2])
            else:
                funciones.borrarPantalla()
                print(f"\n\t.✦📜 E-mail y/o contraseña incorrectas, vuelve a intentarlo...")
                funciones.arte()
                funciones.esperarTecla() 
                funciones.borrarPantalla()
        elif op=="3" or op=="SALIR":
            funciones.borrarPantalla()
            funciones.salir()
            op= False
        else:
            funciones.borrarPantalla()
            print("Pon una opción válida...")
            funciones.arte()
            op=True
            funciones.esperarTecla
            funciones.borrarPantalla()

def main_menu(usuario_id,biblioteca):
    
    while True:
        funciones.menuM(biblioteca)
        op=input("\t\t Qué deseas hacer? (solo el numero): ").strip()
        
        if op=="1":
            funciones.borrarPantalla()
            estanteria.anadir(usuario_id)
            funciones.esperarTecla()
            funciones.borrarPantalla()
        elif op=="2":
            funciones.borrarPantalla()
            estanteria.mostrar(usuario_id)
            funciones.esperarTecla()
            funciones.borrarPantalla()
        elif op=="3":
            funciones.borrarPantalla()
            estanteria.modificar(usuario_id)
            funciones.esperarTecla()
            funciones.borrarPantalla()
        elif op=="4":
            funciones.borrarPantalla()
            estanteria.buscar(usuario_id)
            funciones.esperarTecla()
            funciones.borrarPantalla()
        elif op=="5":
            funciones.borrarPantalla()
            estanteria.borrarL(usuario_id)
            funciones.esperarTecla()
            funciones.borrarPantalla()
        elif op=="6":
            funciones.borrarPantalla()
            estanteria.borrarT(usuario_id)
            funciones.esperarTecla()
            funciones.borrarPantalla()
        elif op=="7":
            funciones.borrarPantalla()
            funciones.exportar(usuario_id,biblioteca)
            funciones.borrarPantalla()
            funciones.esperarTecla()
        elif op=="8":
            funciones.borrarPantalla()
            #para que se vea bonito :)
            funciones.salir()
            funciones.borrarPantalla()
            funciones.esperarTecla()
            opcion=False
        else:
            funciones.borrarPantalla()
            print("Opción no válida. vuelve a intentarlo...")
            funciones.arte()
            funciones.borrarPantalla()
            funciones.esperarTecla()




if __name__ == "__main__":
    main() 