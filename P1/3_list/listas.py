#1 crear lista de numeros e imprimir el contenida
numeros=[1,2,3,4,5]
print(numeros)

#2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
palabras=("hola","adios","si","no","idk","hola")
buscar=input("Dame la palabra a buscar: ")
if buscar in palabras:
    print("sí esta la palabra en la lista")
else:
    print("no está la palabra en la lista")


#3 añadir elementos a la lista
numeros.append(6)
print(numeros)

#4 crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
    ["mama","1234567890"],
    ["papa","0987654321"],
    ["hermano","1122334455"],
    ["amigo","5566778899"]
]
print(agenda)
print("nuevo contacto: ")
nombre=input("nombre: ")
telefono=input("telefono: ")
agenda.append([nombre, telefono])
print(agenda)

for contacto in agenda:
    print(f"Nombre: {contacto[0]}, Telefono: {contacto[1]}")

