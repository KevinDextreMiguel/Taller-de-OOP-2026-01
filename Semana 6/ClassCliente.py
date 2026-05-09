class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, correo, preferente):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.preferente = preferente

    def mostrar_info(self):
        print("="*20)
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Cliente preferente: {'Sí' if self.preferente else 'No'}")

    # setters y getters

    #setters
    def set_dni(self, dni):
        self.dni = dni

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_correo(self, correo):
        self.correo = correo

    def set_preferente(self, preferente):
        self.preferente = preferente

    #getters
    def get_dni(self):
        return self.dni
    def get_nombre(self):
        return self.nombre
    def get_direccion(self):
        return self.direccion
    def get_telefono(self):
        return self.telefono
    def get_correo(self):
        return self.correo
    def get_preferente(self):
        return self.preferente
