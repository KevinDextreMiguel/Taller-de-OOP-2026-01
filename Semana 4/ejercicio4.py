def ingresa_anio():
    anio = -1
    while anio < 0:
        try:
            anio = int(input("Año: "))
        except:
            print("Debe ser enetro")
    
    return anio

def diccionario():
    mi_diccionario = {
        0:"Mono",
        1:"Gallo",
        2:"Perro",
        3:"Cerdo",
        4:"Rata",
        5:"Buey",
        6:"Tigre",
        7:"Liebre",
        8:"Dragon",
        9:"Serpiente",
        10:"Caballo",
        11:"Oveja"
    }

    return mi_diccionario

def horoscopo_chino(mi_diccionario,anio):
    residuo = anio % 12
    print(f"El año es: {anio} y estamos en año de del (la) {mi_diccionario[residuo]}")


#
anio = ingresa_anio()
mi_diccionario = diccionario()
horoscopo_chino(mi_diccionario,anio)
