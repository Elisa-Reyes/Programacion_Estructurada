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
                
            