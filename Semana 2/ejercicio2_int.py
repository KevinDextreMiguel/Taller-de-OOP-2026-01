def pedir_numero():
    n = int(input("Ingresa N: "))

    return n

def descomponer(n):
    u = n % 10
    d = n // 10 % 10
    c = n // 100

    return u,d,c


def realizar_calculos(n1,n2):
    u1 , d1 , c1 = descomponer(n1)
    u2 , d2 , c2 = descomponer(n2)

    print(f"u1 = {u1}, d1 = {d1}, c1 = {c1}, u2 = {u2}, d2 = {d2}, c2 = {c2}")

    invertido_n1 = u1 * 100 + d1 * 10 + c1
    invertido_n2 = u2 * 100 + d2 * 10 + c2

    print(f"N1 invertido: {invertido_n1}")
    print(f"N2 invertido: {invertido_n2}")

    suma_todo = n1 + n2 + invertido_n1 + invertido_n2

    print(f"Suma de todo: {suma_todo}")

    unir_dos_numeros = n1 * 1000 + invertido_n2

    print(f"caso D: {unir_dos_numeros}")


n1 = pedir_numero()
n2 = pedir_numero()
realizar_calculos(n1,n2)
