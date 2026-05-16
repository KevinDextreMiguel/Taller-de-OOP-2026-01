import random
#u202502678@upc.edu.pe -> u202502678  @upc.edu.pe
def pedir_correo():
    correo = ''
    while '@' not in correo or '.' not in correo:
        correo = input('Introduce tu correo electrónico: ')
    return correo

def validar_contrasenia(contrasenia):
    if len(contrasenia) < 8:
        return False
    
    cont_numero = contador_mayuscula = contador_minuscula = contador_caracter_especial = 0

    for caracter in contrasenia:
        if caracter.isdigit():
            cont_numero += 1
        elif caracter.isupper():
            contador_mayuscula += 1
        elif caracter.islower():
            contador_minuscula += 1
        elif caracter in '@,_$':
            contador_caracter_especial += 1

    if cont_numero > 0 and contador_mayuscula > 0 and contador_minuscula > 0 and contador_caracter_especial > 0:
        return True
    else:
        return False

def pedir_contrasenia():
    contrasenia = ''
    while True:
        contrasenia = input('Introduce tu contraseña: ')
        if validar_contrasenia(contrasenia):
            break
        print('La contraseña no cumple con los requisitos. Inténtalo de nuevo.')
    return contrasenia


def registrar():
    correo = pedir_correo()
    lista = correo.split('@')
    usuario = lista[0]
    dominio = lista[1]
    contrasenia = pedir_contrasenia()
    pin = random.randint(100, 999)

    dic_correos[correo] = (usuario, dominio, contrasenia, pin)
    print(f'Correo registrado: {correo}')

def mostrar_correos():
    for clave, valor in dic_correos.items():
        print(f'Correo: {clave}, Usuario: {valor[0]}, Dominio: {valor[1]}, Contraseña: {valor[2]}, PIN: {valor[3]}')    

def eliminarcorreo():
    correo = input('Introduce el correo que deseas eliminar: ')
    pin = int(input('Introduce el PIN asociado al correo: '))
    encontrar = False    
    for clave, valor in dic_correos.items():
        if clave == correo and valor[3] == pin:
            dic_correos.pop(clave)
            dic_correos.remove(clave)
            encontrar = True    
            break
    if  encontrar:
        print(f'Correo {correo} eliminado.')
    else:
        print('Correo o PIN incorrecto. No se pudo eliminar el correo.')

def main():
    while True:
        print('1. Registrar correo')
        print('2. Mostrar correos registrados')
        print('3. Eliminar correo')
        print('4. Salir')
        opcion = input('Selecciona una opción: ')
        
        if opcion == '1':
            registrar()
        elif opcion == '2':
            mostrar_correos()
        elif opcion == '3':
            eliminarcorreo()
        elif opcion == '4':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Inténtalo de nuevo.')



dic_correos = {}
main()
