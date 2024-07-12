import funciones as fn
#geometric_mean()

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","”Francisco Díaz","Elena Fernández"]
sueldos_trabajadores = {}
while True:
    try:
        print("0. Inicializar los sueldos")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos") 
        print("5. Salir del programa")
        opcion = int(input("Ingrese una opcion del menu: "))
        if(opcion == 0):
            for trabajador in trabajadores:
                sueldos_trabajadores[trabajador] = 0
        elif(opcion == 1):
            if not sueldos_trabajadores:
                print("Inicialize sueldos")
            else:
                sueldos_trabajadores = fn.asignar_sueldos(trabajadores)
        elif(opcion == 2):
            if not sueldos_trabajadores:
                print("Inicialize sueldos")
            else:
                fn.clasificacion_sueldos(sueldos_trabajadores,trabajadores)
        elif(opcion == 3):
            if not sueldos_trabajadores:
                print("Inicialize sueldos")
            else:
                fn.estadisticas_sueldos(sueldos_trabajadores,trabajadores)
        elif(opcion == 4):
            if not sueldos_trabajadores:
                print("Inicialize sueldos")
            else:
                fn.reporte_sueldos(sueldos_trabajadores,trabajadores)
        elif(opcion == 5):
            print("Finalizando el programa")
            print("Desarrolado por Vicente Bravo")
            print("Rut 20.522.031-3")
            break
        else:
            print("Elija una de las 6 opciones")
    except:
        print("Opcion no valida")