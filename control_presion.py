# Modulo de control de presion en red de gas natural (XMLP010BC71F)


def ejecutar_control_presion(presion=2.0):
    for lectura in range(1, 11):
        if presion >= 6.0:
            print(
                f"Lectura {lectura} ({presion:.1f} Bar) - "
                "CRÍTICO: Ruptura inminente. Abortar."
            )
            break
        elif presion < 2.0:
            print(
                f"Lectura {lectura} ({presion:.1f} Bar) - "
                "Acción: Inyectando presion a la red."
            )
            presion += 0.5
        elif 2.0 <= presion <= 4.5:
            print(
                f"Lectura {lectura} ({presion:.1f} Bar) - "
                "Acción: Flujo nominal estabilizado."
            )
            presion += 0.1
        else:
            print(
                f"Lectura {lectura} ({presion:.1f} Bar) - "
                "Acción: Purga de emergencia abierta."
            )
            presion -= 0.8

    return presion
