class Pasajero:
 
    def __init__(self, numero_pasaporte, nombre, edad, tipo_asiento):
        self.__numero_pasaporte = numero_pasaporte
        self.__nombre = nombre
        self.__edad = edad
        self.__tipo_asiento = tipo_asiento
    
    def mostrar(self):
        print(f"Número de Pasaporte: {self.__numero_pasaporte}")
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"Tipo de Asiento: {self.__tipo_asiento}")
    
    @property
    def numero_pasaporte(self):
        return self.__numero_pasaporte
    @numero_pasaporte.setter
    def numero_pasaporte(self, numero_pasaporte):
        self.__numero_pasaporte = numero_pasaporte
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def tipo_asiento(self):
        return self.__tipo_asiento
    @tipo_asiento.setter
    def tipo_asiento(self, tipo_asiento):
        self.__tipo_asiento = tipo_asiento



class Vuelo:
    def __init__(self, numero_vuelo, hora_salida, hora_llegada, ciudad_partida, ciudad_llegada):
        self.__numero_vuelo = numero_vuelo
        self.__hora_salida = hora_salida
        self.__hora_llegada = hora_llegada
        self.__ciudad_partida = ciudad_partida
        self.__ciudad_llegada = ciudad_llegada
        self.__asientos_primera_clase = []
        self.__asientos_turista = []
    
    def mostrar_info(self):
        print(f"Número de Vuelo: {self.__numero_vuelo}")
        print(f"Hora de Salida: {self.__hora_salida}")
        print(f"Hora de Llegada: {self.__hora_llegada}")
        print(f"Ciudad de Partida: {self.__ciudad_partida}")
        print(f"Ciudad de Llegada: {self.__ciudad_llegada}")
    
    def agregar_pasajero(self, pasajero):
        if len(self.__asientos_primera_clase) < 8 and pasajero.tipo_asiento == "Primera Clase":
            self.__asientos_primera_clase.append(pasajero)
        elif len(self.__asientos_turista) < 92 and pasajero.tipo_asiento == "Turista":
            self.__asientos_turista.append(pasajero)
        else:
            print("No hay asientos disponibles para el tipo de asiento seleccionado.")
    
    def mostrar_pasajeros(self):
        print("Pasajeros en Primera Clase:")
        for pasajero in self.__asientos_primera_clase:
            pasajero.mostrar()
            print("-" * 20)
        
        print("Pasajeros en Turista:")
        for pasajero in self.__asientos_turista:
            pasajero.mostrar()
            print("-" * 20)

    @property
    def numero_vuelo(self):
        return self.__numero_vuelo
    @numero_vuelo.setter
    def numero_vuelo(self, numero_vuelo):
        self.__numero_vuelo = numero_vuelo
    
    @property
    def hora_salida(self):
        return self.__hora_salida
    @hora_salida.setter
    def hora_salida(self, hora_salida):
        self.__hora_salida = hora_salida
    
    @property
    def hora_llegada(self):
        return self.__hora_llegada
    @hora_llegada.setter
    def hora_llegada(self, hora_llegada):
        self.__hora_llegada = hora_llegada
    
    @property
    def ciudad_partida(self):
        return self.__ciudad_partida
    @ciudad_partida.setter
    def ciudad_partida(self, ciudad_partida):
        self.__ciudad_partida = ciudad_partida

    @property
    def ciudad_llegada(self):
        return self.__ciudad_llegada
    @ciudad_llegada.setter
    def ciudad_llegada(self, ciudad_llegada):
        self.__ciudad_llegada = ciudad_llegada



objeto_vuelo = Vuelo("AV123", "08:00", "12:00", "Ciudad A", "Ciudad B")

pasajero1 = Pasajero("P123456", "Juan Pérez", 30, "Primera Clase")
pasajero2 = Pasajero("P654321", "María Gómez", 25, "Turista")
pasajero3 = Pasajero("P789012", "Carlos Rodríguez", 40, "Primera Clase")
pasajero4 = Pasajero("P210987", "Ana Martínez", 28, "Turista")
objeto_vuelo.agregar_pasajero(pasajero1)
objeto_vuelo.agregar_pasajero(pasajero2)
objeto_vuelo.agregar_pasajero(pasajero3)
objeto_vuelo.agregar_pasajero(pasajero4)

objeto_vuelo.mostrar_info()
objeto_vuelo.mostrar_pasajeros()
