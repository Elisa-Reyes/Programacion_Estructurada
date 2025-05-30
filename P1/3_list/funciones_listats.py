'''
lists (array)
son colecciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable. Permite miembros duplicados

'''

import os
os.system ("cls")

#funciones mas comunes en las listas
paises=["Mexico","España","Brasil","Canada"]

numeros=[23,45,8,24]

varios=["hola",3.1416,33,True]

#imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#recorrer la lista
#primer forma
print(" ")
print("primera forma")

for i in paises:
    print(i)

#segunda forma
print(" ")
print("segunda forma")

for i in range (0,len(paises)):
    print(paises[i])
    #entre corchetes [i] para que el numero sea la posision y no solo de un numero sine un pais

print(" ")
print("otro ejemplo")

lista=""
for i in range(0,len(paises)):
    lista+=f"[{paises[i]}],"
    print(lista)

#ordenar elementos de una lista
print(" ")
print("listas ordenadas")

paises.sort()
print(paises)
numeros.sort()
print(numeros)
#varios.sort no se puede porque no se comparan diferente tipos de datos

#darle la vuelta a una lista
print(" ")
print("darle la vuelta a listas")

paises.reverse()
print(paises)
varios.reverse()
print(varios)

#agregar, insertar, añadir un elemento a una lista
#primer forma (recomendada porque cuando agregas informacion a una bd se ingresa al final)
print(" ")
print("añadir cosas a la lista")

paises.append("Honduras")
print(paises)

#segunda forma (lo añade al inicio)
print(" ")
print("segunda forma")

paises.insert(1,"Honduras")

#luego de hacer un sort, se acomoda
paises.sort()
print(paises)

#eliminar, borrar, suprimir, un elemento de una lista
#primer forma
print(" ")
print("Borrar primera forma")
paises.pop(4)
print(paises)

#segunda se escribe igual
print(" ")
paises.remove("Honduras")
print(paises)

#añadir a una lista especifica
print(" ")
print("añadir a una lista especifica")

print("escrito de la misma forma")
print(paises)
resp="Brasil" in paises
print(resp)

print("escrito diferente")
print("brasil" in paises)

#contar el numero de veces que aparece un elemento dentro de la lista
print(" ")
print("numero de veces")
print(numeros)

cuantos=numeros.count(23)
print(cuantos)

#conocer la posicion en la que se encuentra un elemento de la lista
print(" ")
print("posicion en la lista")
print(paises)
posicion=paises.index("Canada") #las funciones van en parentesis
print(f"el valor de canada lo encontro en: {posicion}")

#unir el contenido de una lista con otra

print(numeros)
numeros2=[100,200]
print(numeros2)

#crear a partir de las listas de numeros 1 y 2 un resultante y mostrar el contenido ordenado descendentemente
numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)