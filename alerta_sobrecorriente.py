# Modulo de alertas por sobrecorriente - Subestacion electrica

historial_corriente = [1.5, 2.0, 12.8, 4.5, 30.2, 1.1] * 5000
historial_indexado = set(historial_corriente)


def buscar_valor_critico_relevador(valor, mostrar_alerta=True):
    existe = valor in historial_indexado

    if existe and valor > 25.0 and mostrar_alerta:
        print(
            "ALERTA DE SOBRECORRIENTE DETECTADA EN LA SUBESTACIÓN: "
            "EL VALOR SUPERA LOS LÍMITES"
        )
    elif mostrar_alerta:
        print(f"Lectura {valor} A dentro de parámetros normales.")

    return existe
