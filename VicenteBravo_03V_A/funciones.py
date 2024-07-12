import random
import statistics 
import csv
def asignar_sueldos(trabajadores):
    sueldos_trabajadores = {}
    for trabajador in trabajadores:
        sueldos_trabajadores[trabajador] = random.randint(300000,2500000)
    return sueldos_trabajadores
def clasificacion_sueldos(sueldos_trabajadores,trabajadores):
    sueldos_menores_800mil = {}
    sueldos_entre_800mil_2millones = {}
    sueldos_mayores_2millones = {}
    contador_sueldos_menores_800mil = 0
    contador_sueldos_entre_800mil_2millones = 0
    contador_sueldos_mayores_2millones = 0
    for trabajador in trabajadores:
        if(sueldos_trabajadores[trabajador] < 800000):
            sueldos_menores_800mil[trabajador] = sueldos_trabajadores[trabajador]
            contador_sueldos_menores_800mil += 1
        elif(sueldos_trabajadores[trabajador] > 800000 and sueldos_trabajadores[trabajador] < 2000000):
            sueldos_entre_800mil_2millones[trabajador] = sueldos_trabajadores[trabajador]
            contador_sueldos_entre_800mil_2millones += 1
        else:
            sueldos_mayores_2millones[trabajador] = sueldos_trabajadores[trabajador]
            contador_sueldos_mayores_2millones += 1
    print(sueldos_trabajadores)
    print("Sueldos menores a $800.000 TOTAL: ",contador_sueldos_menores_800mil)
    print("")
    print("Nombre empleado      Sueldo")
    for trabajador in sueldos_menores_800mil:
        print(f"{trabajador}      {sueldos_menores_800mil[trabajador]}")
    print("")
    print("Sueldos entre $800.000 y $2.000.000 TOTAL: ",contador_sueldos_entre_800mil_2millones)
    print("")
    print("Nombre empleado      Sueldo")
    for trabajador in sueldos_entre_800mil_2millones:
        print(f"{trabajador}      {sueldos_entre_800mil_2millones[trabajador]}")
    print("")
    print("Sueldos superiores a $2.000.000 TOTAL: ",contador_sueldos_mayores_2millones)
    print("")
    print("Nombre empleado      Sueldo")
    for trabajador in sueldos_mayores_2millones:
        print(f"{trabajador}      {sueldos_mayores_2millones[trabajador]}")

def estadisticas_sueldos(sueldos_trabajadores,trabajadores):
    lista_valores_sueldos = list(sueldos_trabajadores.values())
    print(lista_valores_sueldos)
    print(f"El sueldo más alto es ${max(lista_valores_sueldos)}")
    print(f"El sueldo más bajo es ${min(lista_valores_sueldos)}")
    suma = 0
    for trabajador in trabajadores:
        suma += sueldos_trabajadores[trabajador]
    promedio = suma / len(lista_valores_sueldos)
    print("El sueldo promedio es $",promedio)
    promedio_geometrico = statistics.geometric_mean(lista_valores_sueldos)
    print("La media geometrica es : ",promedio_geometrico)
def reporte_sueldos(sueldos_trabajadores,trabajadores):
    lista_sueldos_finales = []
    print("Nombre empleado      Sueldo Base     Descuento Salud     Descuento AFP       Sueldo Líquido ")
    for trabajador in trabajadores:
        print(trabajador,end ="        ")
        sueldo = sueldos_trabajadores[trabajador]
        print(sueldo,end ="        ")
        descuento_salud = (sueldo*7)/100
        print(descuento_salud,end ="        ")
        descuento_afp = (sueldo*14)/100
        print(descuento_afp,end ="        ")
        sueldo_liquido = sueldo
        sueldo_liquido -= descuento_salud
        sueldo_liquido -= descuento_afp
        print(sueldo_liquido)
        lista_sueldo = []
        lista_sueldo.append(trabajador)
        lista_sueldo.append(sueldo)
        lista_sueldo.append(descuento_salud)
        lista_sueldo.append(descuento_afp)
        lista_sueldo.append(sueldo_liquido)
        lista_sueldos_finales.append(lista_sueldo)
    nombre = "archivo.csv"
    encabezado =["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"]
    with open(f"{nombre}","w",newline = "") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)
        for lista in lista_sueldos_finales:
            escritor.writerow(lista)
