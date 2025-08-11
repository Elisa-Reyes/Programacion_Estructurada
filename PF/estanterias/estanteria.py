from conexionBD import *
import funciones

#Hay que mantener todo junto para ver errores

def anadir(usuario_id):
    print("\n\t\tAñadir un libro nuevo")
    titulo=input("Titulo del libro: ").strip().lower()
    autor=input("Ingrese el autor: ").strip().lower()
    clas=input("Clasificación: ").strip().lower()
    genero=input("Ingrese el género: ").strip().lower()
    estan=input("Ingrese la estanterá en donde está: ").strip().lower()
    try:
        cursor.execute("insert into libros (usuario_id,titulo,autor,clasificacion,genero,estanteria,fecha) values (%s,%s,%s,%s,%s,%s,NOW())",(usuario_id,titulo,autor,clas,genero,estan))
        conexion.commit()
        print(f"Libro {titulo} guardado con éxito! *🫧")
        return True
    except Exception as e:
        print(e)
        funciones.arte()
        return False
    
def mostrar(usuario_id):
    cursor.execute("SELECT * FROM libros WHERE usuario_id = %s", (usuario_id,))
    todos_lib=cursor.fetchall()
    if len(todos_lib)>0:
        print("\n\tTodos los Libros en la Biblioteca")
        print(f"{'ID':<10}{'Titulo':<15}{'Autor':<15}{'Clasificacion':<15}{'Género':<15}{'Estantería':<15}{'Fecha':<15}")
        print(f"\033[94m-\033[0m"*100)
        for fila in todos_lib:
            fecha=fila[7].strftime('%d/%m/%Y') if fila[7] else 'Sin fecha'
            print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}{fecha:<15}")
        print(f"\033[94m-\033[0m"*100)
    else:
        print("No hay Libros...")
        funciones.arte()
            
def modificar(usuario_id):
    print("\n\tModificar un libro")
    
    id=input("ID del titulo a modificar: ").strip()
    cursor.execute("SELECT id FROM libros WHERE id = %s and usuario_id =%s", (id,usuario_id))
    libros_lista=cursor.fetchone()
    if libros_lista:
        titulo=input("Titulo del libro: ").strip().lower()
        autor=input("Ingrese el autor: ").strip().lower()
        clas=input("Clasificación: ").strip().lower()
        genero=input("Ingrese el género: ").strip().lower()
        estan=input("Ingrese la estanterá en donde está: ").strip().lower()
        try:
            cursor.execute("update libros set titulo=%s,autor=%s,clasificacion=%s,genero=%s,estanteria=%s,fecha=now() where id=%s",(titulo,autor,clas,genero,estan,id))
            conexion.commit()
            print("Libro modificado correctamente *🫧")
            return True
        except Exception as e:
            print(e)
            funciones.arte()
            return False
    else:
        funciones.borrarPantalla
        print("\n\tEste libro no existe...")
        funciones.arte()

def buscar(usuario_id):
    print("Buscar Libro en Especifico")
    nombre=input("💖.- Título del libro a buscar: ").lower().strip()
    try:
        cursor.execute("select * from libros where usuario_id=%s and titulo like %s", (usuario_id,nombre))
        libros_lista=cursor.fetchall()
        if libros_lista:
            print(f"{'ID':<10}{'Titulo':<15}{'Autor':<15}{'Clasificacion':<15}{'Género':<15}{'Estantería':<15}{'Fecha':<15}")
            print(f"\033[94m-\033[0m"*100)
            for fila in libros_lista:
                fecha=fila[7].strftime('%d/%m/%Y') if fila[7] else 'Sin fecha'
                print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}{fecha:<15}")
            print(f"\033[94m-\033[0m"*100)
        else:
            print("No está :C")
            funciones.arte()
    except Exception as e:
        print(e)
        funciones.arte()
        return []
    
def borrarL(usuario_id):
    print("\n\tBorrar libro")
    id=input("🍓.- ID del libro a borrar: ").strip()
    cursor.execute("select id from libros where usuario_id = %s", (usuario_id,))
    libros=cursor.fetchall()
    if not libros:
        print("\n\tNo tienes libros registrados para borrar...")
        funciones.arte()
        return False
    else:
        try:
            resp=input("\n\t🫧.- Estás segura(o)? (si/no) ").strip().lower()
            if resp=="si":
                cursor.execute("delete from libros where id=%s",(id,))
                conexion.commit()
                print("Libro borrado correctamente *🫧")

            return True
        except Exception as e:
            print(e)
            funciones.arte()
            return False
        
def borrarT(usuario_id):
    resp=input("🍒.- Vas a eliminar todo, estás segura(o)? (si/no) ").strip().lower()
    if resp=="si":
        try:
         cursor.execute("delete from libros where usuario_id=%s",(usuario_id,))
         conexion.commit()
         print("Se borraron todos los libros correctamente... 💖")
         return True
        except Exception as e:
            print(e)
            funciones.arte()
            return False
