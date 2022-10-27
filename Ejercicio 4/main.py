def main():
    pagoDeLaEmpresa = 0
    numeroTrabajadores = input('Ingrese el total de trabajadores: ')

    if numeroTrabajadores.isdigit() == True:
        numeroTrabajadores = int(numeroTrabajadores)
    else:
        print("\nIngrese una opción válida por favor. \n")

    for i in range(1, numeroTrabajadores + 1, 1):
        print('Proceso #' + str(i))
        
        horasTrabajadas = input('Ingrese el valor de las horas trabajadas: ')
        if horasTrabajadas.isdigit() == True:
            horasTrabajadas = int(horasTrabajadas)
        else:
            print("\nIngrese una opción válida por favor. \n")
        
        pagoPorHora = input('Ingrese el valor de pago por hora: ')
        if pagoPorHora.isdigit() == True:
            pagoPorHora = int(pagoPorHora)
        else:
            print("\nIngrese una opción válida por favor. \n")

        sueldoSemanal = pagoPorHora * horasTrabajadas
        pagoDeLaEmpresa = pagoDeLaEmpresa + sueldoSemanal
        print('Valor del sueldo semanal: ' + str(sueldoSemanal))

    print('Valor del pago de la empresa: ' + str(pagoDeLaEmpresa))

main()