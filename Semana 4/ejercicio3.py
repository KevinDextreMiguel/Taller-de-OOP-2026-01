def definir_texto():
    texto = """¡Oh! Que madre tan bella. ¿Será que La madre de Juan es hermana de Pedro? 
    Juan va con ella a todos lados; es decir no la deja sola ni para ir al mercado. 
    Juan le dice a su madre que compre piña, mango, melón, patilla porque son 
    nutritivos. 
    La madre de Juan le enseña las vocales: a, e, i, o, u. 
    En la casa de Juan hay muchos colores: azul, amarillo, rojo, verde… 
    La madre de Juan le enseña que Simón Bolívar dijo: 
    "Un ser sin estudio es un ser incompleto". """

    return texto

def imprimir(texto):
    print('='*20)
    print(texto)

def quitar_signos_convertir_minuscula(texto):
    texto_sin_signos = ''
    signos = '¡!.¿?;,":'
    for letra in texto:
        if letra in signos:
            continue
        else:
            texto_sin_signos += letra
    
    texto_sin_signos = texto_sin_signos.lower()
    imprimir(texto_sin_signos)

    dic_contar = {}
    lista_texto = texto_sin_signos.split()
    for palabra in lista_texto:
        dic_contar[palabra] = dic_contar.get(palabra,0) + 1

    return dic_contar

def ordenar(clave_valor):
    return clave_valor[1]


def ordenar_cantidad(dic_contar):
    dic_texto_ordenado = dict(sorted(dic_contar.items(),key=ordenar,reverse=True))
    for clave,valor in dic_texto_ordenado.items():
        if valor > 1:
            print(f'{clave}: {valor}')


texto = definir_texto()
imprimir(texto)
dic_contar = quitar_signos_convertir_minuscula(texto)
ordenar_cantidad(dic_contar)
