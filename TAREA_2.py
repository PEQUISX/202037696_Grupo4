

presion=2

for lectura in range(10):
    if presion >= 6.0:
       print("CRiTICO: Ruptura inminente. Abortar.")
       break
    elif presion < 2.0:
        print("Accion: Inyectando presión a la red")
        presion += 0.5
    elif presion >= 2.0 and presion <= 4.5:
         print("Accion: Flujo nominal estabilizado")
         presion += 0.1
    else:
      print("Accion: Purga de emergencia abierta")
      presion -= 0.8

