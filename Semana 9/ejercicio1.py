class Encomienda:
    dicc_encomiendas = {}

    def __init__(self,codigo, remitente, destinatario, direccion_entrega, peso_kg, volumen_m3, costo_kg, costo_m3):
        self.__codigo = codigo
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__direccion_entrega = direccion_entrega
        self.__peso_kg = peso_kg
        self.__volumen_m3 = volumen_m3
        self.__costo_kg = costo_kg
        self.__costo_m3 = costo_m3

    def calcular_costo_peso(self):
        return self.__peso_kg * self.__costo_kg

    def calcular_costo_volumen(self):
        return self.__volumen_m3 * self.__costo_m3

    def calcular_valor_envio(self):
        return self.calcular_costo_peso() + self.calcular_costo_volumen()

    def mostrar(self):
        print(f"Código: {self.__codigo}")
        print(f"Remitente: {self.__remitente}")
        print(f"Destinatario: {self.__destinatario}")
        print(f"Dirección de Entrega: {self.__direccion_entrega}")
        print(f"Peso en Kg: {self.__peso_kg}")
        print(f"Volumen en m3: {self.__volumen_m3}")
        print(f"Costo por Kg: {self.__costo_kg}")
        print(f"Costo por m3: {self.__costo_m3}")
        print(f"Costo por Peso: {self.calcular_costo_peso()}")
        print(f"Costo por Volumen: {self.calcular_costo_volumen()}")
        print(f"Valor del Envío: {self.calcular_valor_envio()}")

    def agregar_encomienda(self,objeto_encomienda):
        self.dicc_encomiendas[objeto_encomienda.__codigo] = objeto_encomienda
    
    def mostrar_encomienda(self):
        for encomienda in self.dicc_encomiendas.values():
            print("="*20)
            encomienda.mostrar()

    @property
    def codigo(self):
       return self.__codigo
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @property
    def remitente(self):
        return self.__remitente
    @remitente.setter
    def remitente(self, remitente):
        self.__remitente = remitente
    
    @property
    def destinatario(self):
        return self.__destinatario
    @destinatario.setter
    def destinatario(self, destinatario):
        self.__destinatario = destinatario
    
    @property
    def direccion_entrega(self):
        return self.__direccion_entrega
    @direccion_entrega.setter
    def direccion_entrega(self, direccion_entrega):
        self.__direccion_entrega = direccion_entrega

    @property
    def peso_kg(self):
        return self.__peso_kg
    @peso_kg.setter
    def peso_kg(self, peso_kg):
        if peso_kg < 0:
            print("El peso no puede ser negativo")
        else:   
            self.__peso_kg = peso_kg
    
    @property
    def volumen_m3(self):
        return self.__volumen_m3
    @volumen_m3.setter
    def volumen_m3(self, volumen_m3):
        if volumen_m3 < 0:
            print("El volumen no puede ser negativo")
        else:   
            self.__volumen_m3 = volumen_m3
    
    @property
    def costo_kg(self):
        return self.__costo_kg
    @costo_kg.setter
    def costo_kg(self, costo_kg):
        if costo_kg < 0:
            print("El costo por kg no puede ser negativo")
        else:   
            self.__costo_kg = costo_kg

    @property
    def costo_m3(self):
        return self.__costo_m3
    @costo_m3.setter
    def costo_m3(self, costo_m3):
        if costo_m3 < 0:
            print("El costo por m3 no puede ser negativo")
        else:   
            self.__costo_m3 = costo_m3


#crear objetos
encomienda1 = Encomienda("001", "Juan", "Maria", "Calle 123", 10, 0.5, 2, 3)
encomienda2 = Encomienda("002", "Pedro", "Ana", "Avenida 456", 20, 1, 1.5, 2.5)
#agregar encomiendas al diccionario
encomienda1.agregar_encomienda(encomienda1)
encomienda1.agregar_encomienda(encomienda2)
#mostrar encomiendas
encomienda1.mostrar_encomienda()
