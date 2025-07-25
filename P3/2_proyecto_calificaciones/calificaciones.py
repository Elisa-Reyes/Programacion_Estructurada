import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla(): 
    input("Oprime tecla")  

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None
    
def menu_principal():
    print("`n\ \U0001F4DD` .::Sistema de Gestion de Calificaciones::.`\U0001F4DD` \n\t '`\u2705` 1.-Agregar \n\t `\u2705` 2.-Mostrar \n\t `\u2705` 3.-Calcular promedios \n\t `\u2705` 4.-Buscar \n\t `\u2705`5.-Salir")
    option = input("Elige una opcion (1-4): ")
    return option
    
def agregar_calificaciones(datos):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        print("Agregar Calificaciones")
        nombre=input("Nombre: ").upper().strip()
        if nombre in datos:
            print("Este Alumno ya existe")            
        else:
            cal1=input("Calificacion 1 del 1-10: ").strip()
            cal2=float(input("Calificacion 2 del 1-10: ")).strip()
            cal3=float(input("Calificacion 3 del 1-10: ")).strip()
            datos[nombre]=[cal1,cal2,cal3]
            cursor=conexionBD.cursor()
            sql="insert into datos (nombre,cal1,cal2,cal3) values (%s, %s, %s, %s)"
            val=(nombre,cal1,cal2,cal3)
            cursor.execute(sql,val)
            conexionBD.commit()

            print("Accion Realizada con éxito")

def mostrar_calificaciones(datos):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()

        sql="select * from datos"
        cursor.execute(sql)
        registros=cursor.fetchall()
        if len(registros)>0:
            print("\n\t .:: Mostrar Calificaciones ::.\n")
            print(f"{'ID':<10}{'Nombre':<15}{'Calif 1':<15}{'Calif 2':<15}{'Calif 3':<15}")
            print(f"-"*80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            print(f"-"*80)
            cuantos=len(datos)
            print(f"Son {cuantos} alumnos")
        else:
            print("No hay Alumnos :[")

def calcular_promedios(datos):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM datos")
        lista = cursor.fetchall()
        if len(lista)>0:
            print(f"{'Nombre':<15} {'Promedio':<10}")
            print("-" * 40)
            promedio_grupal = 0
            
            for fila in lista:
                nombre = fila[0]
                promedio = round(sum(fila[1:]) / 3, 2)
                print(f"{nombre:<15}{promedio:.2f}")
                promedio_grupal += promedio
            print("-" * 40)
            promedio_grupal = round(promedio_grupal / len(lista), 2)
            print(f"El promedio del grupo es : {promedio_grupal:.2f}")
        else:
            print("No hay Alumnos :[")

def buscar_calificaciones(datos):
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        cursor=conexionBD.cursor()

        print("Buscar Alumnos :D")
        try:
            id = int(input("Escribe el id del alumno a buscar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return
        
        cursor.execute("SELECT * FROM datos where id=%s", (id,))
        lista = cursor.fetchall()
        if len(lista)>0:
            print(f"{'Nombre':<15} {'Promedio':<10}")
            print("-" * 40)
                    
            for fila in lista:
                nombre = fila[1]
                promedio = round(sum(fila[2:]) / 3, 2)
                print(f"{nombre:<15}{promedio:.2f}")
            print("-" * 40)
        else:
            print("No está :C")