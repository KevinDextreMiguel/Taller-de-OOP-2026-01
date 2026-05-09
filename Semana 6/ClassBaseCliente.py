class BaseCliente:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):#es un objeto de la clase Cliente (dni,nombre,....)
        self.clientes.append(cliente)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            cliente.mostrar_info()
    
    def actualizar_cliente(self, nuevo_cliente):
        for i, cliente in enumerate(self.clientes):
            if cliente.get_dni() == nuevo_cliente.get_dni():
                self.clientes[i] = nuevo_cliente
                print(f"Cliente con DNI {nuevo_cliente.get_dni()} actualizado.")

    def eliminar_cliente(self, dni):
        for i, cliente in enumerate(self.clientes):
            if cliente.get_dni() == dni:
                self.clientes.pop(i)
                print(f"Cliente con DNI {dni} eliminado.")

    def buscar_cliente_nombre(self, nombre_buscado):
        for cliente in self.clientes:
            if cliente.get_nombre() == nombre_buscado:
                cliente.mostrar_info()
