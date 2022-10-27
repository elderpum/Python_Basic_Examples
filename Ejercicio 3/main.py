def menu():
    mensualidad = 0
    total = 0

    for i in range(1, 21, 1):
        if i == 1:
            mensualidad = 10
        else:
            mensualidad = mensualidad * 2
        print('El pago en el mes ' + str(i) + 'es de: ' + str(mensualidad))
        total = total + mensualidad
    print('El pago total es de: ' + str(total))

menu()