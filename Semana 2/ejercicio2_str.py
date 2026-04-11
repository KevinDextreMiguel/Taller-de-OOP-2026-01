def pedir_numero():
    n = input("Ingresa N: ")

    return n

def descomponer(n):
    u = n[2]
    d = n[1]
    c = n[0]

    return u,d,c


def realizar_calculos(n1,n2):
    u1 , d1 , c1 = descomponer(n1)
    u2 , d2 , c2 = descomponer(n2)

    print(f"u1 = {u1}, d1 = {d1}, c1 = {c1}, u2 = {u2}, d2 = {d2}, c2 = {c2}")

    invertido_n1 = int(u1) * 100 + int(d1) * 10 + int(c1)
    invertido_n2 = int(u2) * 100 + int(d2) * 10 + int(c2)

    print(f"N1 invertido: {invertido_n1}")
    print(f"N2 invertido: {invertido_n2}")

    suma_todo = int(n1) + int(n2) + invertido_n1 + invertido_n2

    print(f"Suma de todo: {suma_todo}")

    unir_dos_numeros = int(n1) * 1000 + invertido_n2

    print(f"caso D: {unir_dos_numeros}")


n1 = pedir_numero()
n2 = pedir_numero()
realizar_calculos(n1,n2)
