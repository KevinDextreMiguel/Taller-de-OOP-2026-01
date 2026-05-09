class TroncoCono:
    def __init__(self, radio_mayor, radio_menor, altura):
        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor
        self.altura = altura

    def calcular_geratriz(self):
        return ((self.radio_mayor - self.radio_menor) ** 2 + self.altura ** 2) ** 0.5
    
    def calcular_area(self):
        geratriz = self.calcular_geratriz()
        return 3.1416 * (self.radio_mayor**2 + self.radio_menor**2 + (geratriz * (self.radio_mayor + self.radio_menor))) 
    
    def calcular_volumen(self):
        return (1/3) * 3.1416 * self.altura * (self.radio_mayor**2 + self.radio_menor**2 + self.radio_mayor * self.radio_menor)
    
    def mostrar_resultados(self):
        print(f"Geratriz: {round(self.calcular_geratriz(), 4)}")
        print(f"Área: {round(self.calcular_area(), 4)}")
        print(f"Volumen: {round(self.calcular_volumen(), 4)}")


# Ejemplo de uso - objeto 1
def pedir_datos():
    radio_mayor = float(input("Ingrese el radio mayor del tronco de cono: "))
    radio_menor = float(input("Ingrese el radio menor del tronco de cono: "))
    altura = float(input("Ingrese la altura del tronco de cono: "))
    return radio_mayor, radio_menor, altura


radio_mayor, radio_menor, altura = pedir_datos()
tronco1 = TroncoCono(radio_mayor, radio_menor, altura)
tronco1.mostrar_resultados()
