
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprime tecla ──★ ˙🍓 ̟ !!")   

def menu_principal():
    print("\n\t\t\t.::: Sistema de Gestión de Agenda de Contactos :::.\n\n\t\t\t\t\t\t1️⃣ Agregar contacto\n\t\t\t\t\t\t2️⃣ Mostrar todos los contactos\n\t\t\t\t\t\t3️⃣ Buscar contacto por nombre\n\t\t\t\t\t\t4️⃣ Borrar contacto\n\t\t\t\t\t\t3️5 Modificar contacto por nombre\n\t\t\t\t\t\t36. SALIR")
    opcion=input("\n\t\t\t 👉 Elige una opción (1-4): ").upper().strip()
    return opcion


def agregar_contacto(agenda):
    borrarPantalla()
    print("Agregar contactos ⋆.˚🦋༘⋆")
    nombre=input("⟡ Nombre: ").upper().strip()
    if nombre in agenda:
        print("Este contacto ya existe ( ˶ˆᗜˆ˵ )")
    else:
        tel=input("⟡ Telefono: ").strip()
        email=input("⟡ E-mail: ").lower().strip()
        agenda[nombre]=[tel,email]
        print("Accion Realizada con éxito ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("Mostrar Contactos ‧₊ ᵎᵎ 🍒 ⋅ ˚✮")
    if not agenda:
        print("No hay contactos ( ˶°ㅁ°) !!")
    else:
        print(f"{'Nombre':<15} {'Telefono':<15} {'Email':<10}")
        print(f"-"*60)
        for nombre,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")    
        print(f"-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("Mostrar contactos ˚.🎀༘⋆")
    if not agenda:
        print("No hay contactos a mostrar ( ˶°ㅁ°) !!")
    else:
        nombre=input("❀Ingresa el nombre a buscar: ").upper().strip()
        if nombre in agenda:
            for nombres,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
                print(f"{nombres:<15} {datos[0]:<15} {datos[1]:<10}")

def  borrar_contacto(agenda):
    borrarPantalla()
    print("Borrar atributos ִֶָ𓂃 ࣪˖ ִֶָ🐇་༘࿐")
    if not agenda:
        print("No hay contactos a mostrar ( ˶°ㅁ°) !!")

    else:
        nombre=input("꩜Ingresa el nombre a borrar: ").upper().strip()
        if nombre in agenda:
            # for nombres,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
               agenda.pop(nombre)    
        print("Accion realizada con exito ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")

def modificar_contacto(agenda):
    borrarPantalla()
    print("Mostrar contactos ୧ ‧₊˚ 🍮 ⋅ ☆")
    if not agenda:
        print("No hay contactos a mostrar ( ˶°ㅁ°) !!")
    else:
        nombre=input("Ingresa el nombre a modificar: ").upper().strip()
        print(f" ➤Nombre: {[nombre]}")
        if nombre in agenda:
            tel=input("➤Telefono: ").strip()
            email=input("➤E-mail: ").lower().strip()
            agenda[nombre]=[tel,email]
    

