registro_mpu = {
    # Registro Acelerómetro Eje X (Byte Alto)
    "0x3B": {
        "register_name": "ACCEL_XOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    # Se elimina la sobreescritura por clave duplicada de '0x3B',
    # se agrega la llave de apertura '{' faltante en '0x3D' y se asignó
    # el nombre correspondiente al byte alto del eje Y (ACCEL_YOUT_H)
    "0x3D": {
        "register_name": "ACCEL_YOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    # CORRECION: Tipo de dato incorrecto:
    # El 'bit_mask' se cambia de lista [0x00, 0x40] a valor hexadecimal escalar (0x40)
    # El 'sampling_rate' se cambió de texto "100Hz" a entero numérico (100)
    "0x6B": {
        "register_name": "PWR_MGMT_1",
        "bit_mask": 0x40,
        "sampling_rate": 100
    }
}
# 2. Control numérico para evitar bucles infinitos (máximo 3 consultas)
MAX_INTENTOS = 3

for intento in range(1, MAX_INTENTOS + 1):
    entrada = input(f"\n[Consulta {intento}/{MAX_INTENTOS}] Ingrese dirección (ej. 0x3B) o nombre: ").strip()

    # Búsqueda 1: Directa por dirección con .get()
    datos = registro_mpu.get(entrada)

    # Búsqueda 2: Si no coincidió la clave, busca por register_name
    if datos is None:
        for direccion, info in registro_mpu.items():
            if info.get("register_name") == entrada:
                datos = info
                break

    # 3. Mostrar las  especificaciones de forma ordenada
    if datos is not None:
        print(f"-> Nombre del registro : {datos.get('register_name')}")
        print(f"-> Máscara de bits     : {hex(datos.get('bit_mask'))}")
        print(f"-> Tasa de muestreo    : {datos.get('sampling_rate')} Hz")
    else:
        print("-> Registro no encontrado.")

print("\nFin del programa: Límite numérico alcanzado con éxito.")