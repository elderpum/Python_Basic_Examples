import os
from shapely.geometry import Polygon

usuario = 'admin'
password = 'admin'
listaCoordenadas = []

def menu():
    print('########## LOGIN ##########')
    ingresarUsuario = input("Ingresa el usuario: ")
    ingresarPassword = input("Ingresar la contraseña: ")

    if ingresarUsuario == usuario and ingresarPassword == password:
        print('\nBienvenido usuario administrador. \n')
        ingresarWKT()

    else:
        print('\nUsuario o contraseña inválidos, por favor vuelva a intentarlo.\n')
        menu()

def ingresarWKT():
    print('########### INGRESAR GEOMETRIA WKT ##########')
    ingresarCoordenada1 = input("Ingresa la primer coordenada: ")
    if ingresarCoordenada1.isdigit() == True:
        ingresarCoordenada1 = int(ingresarCoordenada1)
    else:
        print("\nIngrese una opción válida por favor. \n")

    ingresarCoordenada2 = input("Ingresa la segunda coordenada: ")
    if ingresarCoordenada2.isdigit() == True:
        ingresarCoordenada2 = int(ingresarCoordenada2)
    else:
        print("\nIngrese una opción válida por favor. \n")

    agruparCoordenadas = (ingresarCoordenada1, ingresarCoordenada2)
    listaCoordenadas.append(agruparCoordenadas)

    preguntarRepeticion = input("¿Desea agregar más coordenadas?: ")
    if preguntarRepeticion == 'Si' or preguntarRepeticion == 'si':
        print()
        ingresarWKT()
    else:
        polygon = Polygon(listaCoordenadas)
        print(polygon.wkt)
        file = open("shape.shp", "w")
        file.write(polygon.wkt)
        file.close()


def ejemplo():
    lista = []

    numero1 = 5
    numero2 = 10
    agrupacion = (numero1, numero2)

    lista.append(agrupacion)

    print(lista)

menu()