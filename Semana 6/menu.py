from ClassBaseCliente import BaseCliente
from ClassCliente import Cliente

def pedir_opcion():
    print("1. Agregar cliente")
    print("2. Mostrar clientes")
    print("3. Actualizar cliente")
    print("4. Eliminar cliente")
    print("5. Buscar cliente por nombre")
    print("6. Salir")

    opcion = -1
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 6:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    return opcion


def pedir_datos_cliente():
    dni = ''
    while not dni.isdigit() or len(dni) != 8:
        dni = input("Ingrese el DNI del cliente (8 dígitos): ")
        if not dni.isdigit() or len(dni) != 8:
            print("DNI no válido. Debe contener exactamente 8 dígitos.")

    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    preferente = int(input("¿Es un cliente preferente? (1/0): "))

    objeto_cliente = Cliente(dni, nombre, direccion, telefono, correo, preferente)
    return objeto_cliente


def main():
    base_cliente = BaseCliente()
    while True:
        opcion = pedir_opcion()
        if opcion == 1:
            cliente = pedir_datos_cliente()
            base_cliente.agregar_cliente(cliente)
            print("Cliente agregado exitosamente.")
        elif opcion == 2:
            base_cliente.mostrar_clientes()
        elif opcion == 3:
            nuevo_cliente = pedir_datos_cliente()
            base_cliente.actualizar_cliente(nuevo_cliente)
        elif opcion == 4:
            dni = input("Ingrese el DNI del cliente a eliminar: ")
            base_cliente.eliminar_cliente(dni)
        elif opcion == 5:
            nombre_buscado = input("Ingrese el nombre del cliente a buscar: ")
            base_cliente.buscar_cliente_nombre(nombre_buscado)
        elif opcion == 6:
            print("Saliendo del programa.")
            break


if __name__ == "__main__":
    main()
