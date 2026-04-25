def pedir_datos():
    medio_trasnporte = ''

    while medio_trasnporte != 'X':
        medio_trasnporte = input("Medio de transporte: ")
        medio_trasnporte = medio_trasnporte.upper()

        if medio_trasnporte != 'X':
            tiempo_duracion = int(input("Tiempo de duración del viaje: "))
            momento_dia = int(input("Momento del día: "))
            ruta_elegida = input("Ruta elegida: ")

            lista_medio_trasnporte.append(medio_trasnporte)
            lista_momento_dia.append(momento_dia)
            lista_tiempo_duracion.append(tiempo_duracion)
            lista_ruta_elegida.append(ruta_elegida)


def cantidad_medio_trasporte():
    contA = contT = contP = 0
    for trasnporte in lista_medio_trasnporte:
        if trasnporte == 'A':
            contA +=1
        elif trasnporte == 'T':
            contT +=1
        else:
            contP +=1
    
    print("Reporte ")
    print(f"Cantidad de usuarios por medio de transporte")
    print(f"Auto propio: {contA}")
    print(f"Privado: {contT}")
    print(f"Transporte público: {contP}")

def ordenar(clave_valor):
    return clave_valor[1]


def momentos_mayor_viaje():
    cont1 = cont2 = cont3 = cont4 = 0
    for momento in lista_momento_dia:
        if momento == 1:
            cont1 +=1
        elif momento == 2:
            cont2 +=1
        elif momento == 3:
            cont3 +=1
        else:
            cont4 +=1
    
    dic_momentos_dia = {'1':cont1, '2':cont2, '3':cont3, '4':cont4}

    dic_momentos_dia_ordenado = dict(sorted(dic_momentos_dia.items(),key=ordenar,reverse=True))
    print("Momentos con mayor cantidad de viajes son: ")
    for clave,valor in dic_momentos_dia_ordenado.items():
        if valor > 0:
            print(f"{clave}", end=', ')


def tiempo_promedio_ruta():
    contA = contB = contC = contO = 0
    sumaA = sumaB = sumaC = sumaO = 0
    proemdioA = proemdioB = proemdioC = proemdioO = 0

    for i in range(len(lista_tiempo_duracion)):
        if lista_ruta_elegida[i] == 'A':
            contA += 1
            sumaA += lista_tiempo_duracion[i]
        elif lista_ruta_elegida[i] == 'B':
            contB += 1
            sumaB += lista_tiempo_duracion[i]
        elif lista_ruta_elegida[i] == 'C':
            contC += 1
            sumaC += lista_tiempo_duracion[i]
        else:
            contO += 1
            sumaO += lista_tiempo_duracion[i]
    
    if contA > 0:
        proemdioA = sumaA / contA
    if contB > 0:
        proemdioB = sumaB / contB
    if contC > 0:
        proemdioC = sumaC / contC
    if contO > 0:
        proemdioO = sumaO / contO

    print("\nTiempo promedio de viaje por ruta son: ")
    print(f"Av. Arequipa: {proemdioA}")
    print(f"Av. Brasil: {proemdioB}")
    print(f"Paseo de la República: {proemdioC}")
    print(f"Otra ruta: {proemdioO}")



#LISTAS
lista_medio_trasnporte = []
lista_momento_dia = []
lista_tiempo_duracion = []
lista_ruta_elegida = []

pedir_datos()
cantidad_medio_trasporte()
momentos_mayor_viaje()
tiempo_promedio_ruta()
