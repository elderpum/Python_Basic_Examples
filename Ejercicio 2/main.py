import sys

montoMayor = []
montoMediano = []
montoPeque = []

def menu():
    print('#####MENÚ TIENDA TIKI TAKA#####')
    print("Selecciona una opción para navegar")
    print("\t1. Realizar una venta")
    print("\t2. Ver el monto de las ventas")
    print("\t2. Salir")
    print("#######################")

    while True:
        opcionMenu = input("Inserta un número para navegar: ")

        if opcionMenu.isdigit() == True:
            opcionMenu = int(opcionMenu)
            if opcionMenu == 1:
                venta()
            if opcionMenu == 2:
                verVentas()
            elif opcionMenu == 3:
                sys.exit()
            else:
                print("\nIngrese una opción válida por favor. \n")
        else:
            print("\nIngrese una opción válida por favor. \n")

def venta():
    montoVenta = input("Ingresa el monto de la venta: ")

    if montoVenta.isdigit() == True:
        montoVenta = int(montoVenta)
        if montoVenta > 1000:
            montoMayor.append(montoVenta)
            print()
            menu()
        elif montoVenta > 500 and montoVenta <= 1000:
            montoMediano.append(montoVenta)
            print()
            menu()
        elif montoVenta <= 500:
            montoPeque.append(montoVenta)
            print()
            menu()
        else:
            print("\nIngrese una opción válida por favor. \n")
            menu()
    else:
        print("\nIngrese una opción válida por favor. \n")
        menu()

def verVentas():
    print('\nVentas mayores a 1000')
    for mayor in montoMayor:
        print('El monto de la venta es de ' + str(mayor))

    print('\nVentas menores o iguales a 1000 pero mayores a 500')
    
    for mediano in montoMediano:
        print('El monto de la venta es de ' + str(mediano))

    print('\nVentas menores o iguales a 500')
    for peque in montoPeque:
        print('El monto de la venta es de ' + str(peque))

menu()