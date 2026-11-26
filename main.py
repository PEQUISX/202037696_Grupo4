# Programa principal - Integracion de modulos industriales

from alerta_sobrecorriente import buscar_valor_critico_relevador
from control_presion import ejecutar_control_presion
from registros_mpu6050 import consultar_registros


def menu():
    print("\n--- Sistema de Monitoreo Industrial ---")
    print("1. Control de presion de gas (XMLP010BC71F)")
    print("2. Consulta de registros del sensor MPU-6050")
    print("3. Verificacion de sobrecorriente en subestacion")
    print("4. Salir")


def main():
    while True:
        menu()
        opcion = input("Seleccione una opcion (1-4): ").strip()

        if opcion == "1":
            ejecutar_control_presion(2.0)
        elif opcion == "2":
            consultar_registros()
        elif opcion == "3":
            dato = input("Ingrese corriente en amperios: ").strip()
            try:
                valor = float(dato)
                buscar_valor_critico_relevador(valor)
            except ValueError:
                print("Valor no válido. Debe ingresar un número.")
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opcion incorrecta, intente de nuevo.")


if __name__ == "__main__":
    main()
