class Laptop:
    def __init__(self, marca, chip, precio_base,pantalla="normal"):
        #Atributos
        self.marca = marca
        self.chip = chip
        self.precio_base = precio_base
        self.pantalla = pantalla
        self.precio_final = precio_base

    def calcular_aumento_chip(self):
        if self.chip == "i5":
           return self.precio_base * 0.1
        elif self.chip == "i7":
            return self.precio_base * 0.15
        return 0

    def calcular_aumento_pantalla(self):
        if self.pantalla == "táctil":
            return self.precio_base * 0.05
        return 0

    def mostrar_info(self):
        print("="*20)
        self.precio_final = self.precio_final + self.calcular_aumento_chip() + self.calcular_aumento_pantalla()
        print(f"Marca: {self.marca}")
        print(f"Chip: {self.chip}")
        print(f"Pantalla: {self.pantalla}")
        print(f"Precio base: ${self.precio_base}")
        print(f"Precio final: ${self.precio_final}")


# Crear objetos de la clase Laptop
laptop1 = Laptop("Dell", "i5", 800, "táctil")
laptop2 = Laptop("HP", "i7", 1200)
laptop3 = Laptop("HP", "i3", 1200)

# Mostrar información de las laptops
laptop1.mostrar_info()
laptop2.mostrar_info()
laptop3.mostrar_info()
