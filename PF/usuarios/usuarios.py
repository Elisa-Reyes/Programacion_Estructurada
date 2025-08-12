from conexionBD import *
import hashlib
import getpass
import funciones

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar():
    print("\n\tNuevo usuario 𖹭")
    nombre=input("\t - ¿Cual es tu nombre?: ").upper().strip()
    usuario=input("\t - Biblioteca: ").upper().strip()
    email=input("\t - Ingresa tu email: ").lower().strip()
    password=getpass.getpass("\t - Ingresa tu contraseña (8 caracteres): ").strip()

    if len(password)>=8 and nombre and usuario and email:
        try:
            contrasena=hash_password(password)
            cursor.execute("insert into usuarios (nombre,usuario,email,password) values (%s,%s,%s,%s)",(nombre,usuario,email,contrasena))
            conexion.commit()
            funciones.borrarPantalla()
            print("Usuario registrado con exito 💖")

            funciones.esperarTecla()
            funciones.borrarPantalla()
            return True
        except Exception as e:
            print(f"Error al registrar: {e}")
            funciones.esperarTecla()
            return False
    else:
        funciones.borrarPantalla()
        print("\n\tEscribe bien tus datos...")
        print("\n\t- La contraseña debe de tener 8 caracteres o más. \n\t- Debes de poner algo.")
        funciones.arte()
        funciones.esperarTecla()
        funciones.borrarPantalla()
        
def login(email,password):
    try:
       cont=hash_password(password)
       cursor.execute("select * from usuarios where email=%s and password=%s",(email,cont)) 
       return cursor.fetchone()
    except Exception as e:
        print(f"{e}")
        funciones.arte()
        return []     
