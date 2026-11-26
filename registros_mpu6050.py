# Modulo de consulta de registros del sensor MPU-6050

MAX_INTENTOS = 3

registro_mpu = {
    "0x3B": {
        "register_name": "ACCEL_XOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000,
    },
    "0x3D": {
        "register_name": "ACCEL_YOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000,
    },
    "0x6B": {
        "register_name": "PWR_MGMT_1",
        "bit_mask": 0x40,
        "sampling_rate": 100,
    },
}


def buscar_registro(entrada):
    clave = entrada.strip().upper()

    for direccion, info in registro_mpu.items():
        if direccion.upper() == clave:
            return info
        if info.get("register_name", "").upper() == clave:
            return info

    return None


def consultar_registros():
    for intento in range(1, MAX_INTENTOS + 1):
        texto = (
            f"\nConsulta {intento}/{MAX_INTENTOS} - "
            "Ingrese dirección (ej. 0x3B) o nombre: "
        )
        entrada = input(texto)
        datos = buscar_registro(entrada)

        if datos is not None:
            print(f"-> Nombre del registro : {datos.get('register_name')}")
            print(f"-> Máscara de bits     : {hex(datos.get('bit_mask'))}")
            print(f"-> Tasa de muestreo    : {datos.get('sampling_rate')} Hz")
        else:
            print("-> Registro no encontrado.")

    print("\nFin de las consultas.")
    