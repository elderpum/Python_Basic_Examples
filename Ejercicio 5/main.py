def main():
    pagoDeLaEmpresa = 0
    numeroTrabajadores = input('Ingrese el total de trabajadores: ')

    if numeroTrabajadores.isdigit() == True:
        numeroTrabajadores = int(numeroTrabajadores)
    else:
        print("\nIngrese una opción válida por favor. \n")

    for i in range(1, numeroTrabajadores + 1, 1):
        print('Proceso #' + str(i))

        diasTrabajados = input('Ingrese la cantidad de dias laburados: ')
        if diasTrabajados.isdigit() == True:
            diasTrabajados = int(diasTrabajados)
        else:
            print("\nIngrese una opción válida por favor. \n")

        horasTrabajadas = input('Ingrese las horas totales de los dias laburados: ')
        if horasTrabajadas.isdigit() == True:
            horasTrabajadas = int(horasTrabajadas)
        else:
            print("\nIngrese una opción válida por favor. \n")

        sueldoSemanal = horasTrabajadas * diasTrabajados
        pagoDeLaEmpresa = pagoDeLaEmpresa + sueldoSemanal
        print('Valor del sueldo semanal: ' + str(sueldoSemanal))

    print('\nValor del pago de la empresa: ' + str(pagoDeLaEmpresa))

main()