import turnos

while 1:
    turno = input("Ingrese: ")
    match turno:
        case "1":
            turnos.informacion_adicional(turnos.perfumes)
        case "2":
            turnos.informacion_adicional(turnos.farmacia)
        case "3":
            turnos.informacion_adicional(turnos.cosmetica)
        case "4":
            print("Saliendo del programa...")
            break
        case _:
            print("Número inválido")