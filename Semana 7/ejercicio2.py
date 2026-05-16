class Laptop:
    def __init__(self, marca, procesador,pantalla):
        self.__marca = marca
        self.__procesador = procesador
        self.__pantalla = pantalla
        self.__precio = 1000
    
    def incrementar_precio_marca(self):
        if self.__marca == "Dell":
            return self.__precio * 0.02
        elif self.__marca == "Acer":
            return self.__precio * 0.01
        else:
            return 0
    
    def incrementar_precio_procesador(self):
        if self.__procesador == "i7":
            return self.__precio * 0.15
        elif self.__procesador == "i5":
            return self.__precio * 0.1
        else:
            return 0
    
    def incmrementar_precio_pantalla(self):
        if self.__pantalla == "táctil":
            return self.__precio * 0.05
        else:
            return 0
    
    def calcular_precio_final(self):
        incremento_marca = self.incrementar_precio_marca()
        incremento_procesador = self.incrementar_precio_procesador()
        incremento_pantalla = self.incmrementar_precio_pantalla()
        precio_final = self.__precio + incremento_marca + incremento_procesador + incremento_pantalla
        return precio_final

    def mostrar_info(self):
        print(f"Marca: {self.__marca}")
        print(f"Procesador: {self.__procesador}")
        print(f"Pantalla: {self.__pantalla}")
        print(f"Precio: ${self.__precio}")
        print(f"Precio final: ${self.calcular_precio_final()}")
    
    #getters
    def get_marca(self):
        return self.__marca
    def get_procesador(self):
        return self.__procesador
    
    #setters
    def set_marca(self, marca):
        self.__marca = marca


class Catalogo:
    def __init__(self):
        self.__laptops = []
    
    def agregar_laptop(self, laptop):
        self.__laptops.append(laptop)
    

    #listar las computadoras ordenadas por precio final
    def listar_por_precio_final(self):
        lista_aux = []

        for laptop in self.__laptops:
            precio_final = laptop.calcular_precio_final()
            lista_aux.append((precio_final, laptop))

        lista_aux.sort(reverse=True)
        for precio_final, laptop in lista_aux:
            laptop.mostrar_info()
            print('-------------------')

    #listar por marca y procesador
    def listar_por_marca_y_procesador(self, marca, procesador):
        for laptop in self.__laptops:
            if laptop.get_marca() == marca and laptop.get_procesador() == procesador:
                laptop.mostrar_info()
                print('-------------------')
    
    #reporte por tipo de procesador
    def reporte_por_tipo_procesador(self):
        cantidad_i7 = cantidad_i5 = cantidad_i3 = 0
        for laptop in self.__laptops:   
            if laptop.get_procesador() == "i7":
                cantidad_i7 += 1
            elif laptop.get_procesador() == "i5":
                cantidad_i5 += 1
            elif laptop.get_procesador() == "i3":
                cantidad_i3 += 1

        print(f"cantidad de i7: {cantidad_i7}")
        print(f"cantidad de i5: {cantidad_i5}")
        print(f"cantidad de i3: {cantidad_i3}")


def opciones():
    print("1. Agregar laptop")
    print("2. Listar laptops por precio final ordenados de menor a mayor")
    print("3. Listar laptops por marca y procesador")
    print("4. Reporte por tipo de procesador")
    print("5. Salir")
    opcion  = -1
    while opcion < 1 or opcion > 5:
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Opción inválida. Por favor, ingresa un número del 1 al 5.")
    return opcion


def main():
    catalogo = Catalogo()
    while True:
        opcion = opciones()
        if opcion == 1:
            marca = input("Ingrese la marca de la laptop: ")
            procesador = input("Ingrese el procesador de la laptop (i7, i5, i3): ")
            pantalla = input("Ingrese el tipo de pantalla de la laptop (táctil o no táctil): ")
            laptop = Laptop(marca, procesador, pantalla)
            catalogo.agregar_laptop(laptop)
        elif opcion == 2:
            catalogo.listar_por_precio_final()
        elif opcion == 3:
            marca = input("Ingrese la marca de la laptop: ")
            procesador = input("Ingrese el procesador de la laptop (i7, i5, i3): ")
            catalogo.listar_por_marca_y_procesador(marca, procesador)
        elif opcion == 4:
            catalogo.reporte_por_tipo_procesador()
        elif opcion == 5:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
