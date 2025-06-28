peliculas=["toy story","dunno","idk","pelicula"]

for i, pelicula in enumerate(peliculas, start=1):
    print(i, pelicula)

    
buscar=input("nombre: ").upper().strip()
encontro=0
if not(buscar in peliculas):
    print("la pelicula no esta")
else:
    for i in range(0,len(peliculas)):
        if buscar==peliculas[i]:
            resp=input("Deseas eliminar esta pelicula? (si/no) ").lower()
            encontro+=1
            if resp=="si":
                peliculas.remove[buscar]
                encontro+=1
                
resp="si"
while resp=="si":
    atributo=input("\n\t ingresa la caracteristica: ")
    valor_atributo=input("\n\t ingresa el valor de la caracteristica: ")
    pelicula.update({f"{atributo}":input(f"ingresa el {atributo}").strip().upper()})

def agregarPeliculas():
    print("\n\t agregar caracteristicas ")
    pelicula.update({f"{input("ingresa la caracteristica: ").lower().strip()}":input("ingresa el valor de la caracteristica: ").strip().upper()})

#modificar tiene que mostrar la primera caracteristica del diccionario, 
#luego preguntar y asi uno por uno si se quiere modificar el valor del atributo

def modificarPeliculas():

    if len(pelicula)==0:
        print("no hay caracteristicas a modificar")
    else:
        for atributo, valor_atributo in pelicula.items():
            print({atributo:valor_atributo})
            resp=input("desea cambiar un atributo? (si/no): ").lower().strip()
            
            if resp=="si":
                nuevo_valor=input(f"escribe el nuevo valor para {atributo}: ")
                pelicula[atributo]=nuevo_valor

    if len(pelicula)==0:
        print("no hay caracteristicas a modificar")
    else:
        for atributo, valor_atributo in pelicula.items():
            print({atributo:valor_atributo})
            resp=input("desea cambiar un atributo? (si/no): ").lower().strip()

            if resp=="si":
                nuevo_valor=input(f"escribe el nuevo valor para {atributo}: ")
                pelicula[atributo]=nuevo_valor
        print("tu atributo se ha actualizado!")
        print(pelicula)
        