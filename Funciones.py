import time

def opciones():
    print('Elija la opción (1, 2 o 3)para hallar la raiz cuadrada')
    time.sleep(3)
    print('1 para enumeración exhaustiva \n 2 para aproximación de soluciones \n 3 para busqueda binaria')
    opcion = int(input('Elija una opción'))
    numero = int(input('Escoja el número al que le va a hallar la raiz'))
    if opcion == 1:
        enumeracion(numero)
    elif opcion == 2:
        aproximacion(numero)
    elif opcion == 3:
        busqueda (numero)
    else:
        print('Escoja una opción válida')
def enumeracion(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aproximacion(objetivo):
    epsilon = 0.001
    paso = epsilon**2 
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        #print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')


def  busqueda(objetivo):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

opciones()

